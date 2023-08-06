import pygltflib
from pygltflib import *

import TrakoDracoPy

import vtk
from vtk.util import numpy_support

import numpy as np
import os

import collections


#
#
# MAP VTK DATATYPE TO GLTF COMPONENT TYPE
#
#
vtkDataType_to_gltfComponentType = {

  vtk.VTK_CHAR: pygltflib.BYTE,
  vtk.VTK_UNSIGNED_CHAR: pygltflib.UNSIGNED_BYTE,
  vtk.VTK_SHORT: pygltflib.SHORT,
  vtk.VTK_UNSIGNED_SHORT: pygltflib.UNSIGNED_SHORT,
  vtk.VTK_INT: pygltflib.UNSIGNED_INT,
  vtk.VTK_UNSIGNED_INT: pygltflib.UNSIGNED_INT,
  vtk.VTK_FLOAT: pygltflib.FLOAT

}

#
#
# MAP VTK NUMBEROFCOMPONENTS TO GLTF TYPE
#
#
vtkNumberOfComponents_to_gltfType = {
  
  1: pygltflib.SCALAR,
  2: pygltflib.VEC2,
  3: pygltflib.VEC3,
  4: pygltflib.VEC4
  # TODO MAT2, MAT3, MAT4

}



def convert(input, config=None, verbose=True):

  extension = os.path.splitext(input)[1].lower()

  if extension == '.vtp':

    r = vtk.vtkXMLPolyDataReader()
    r.SetFileName(input)
    r.Update()
    polydata = r.GetOutput()

  elif extension == '.vtk':

    r = vtk.vtkPolyDataReader()
    r.SetFileName(input)
    r.Update()
    polydata = r.GetOutput()

  else:

    raise Error('Invalid input format.')


  # print(polydata.GetBounds())

  points = numpy_support.vtk_to_numpy(polydata.GetPoints().GetData())
  lines = numpy_support.vtk_to_numpy(polydata.GetLines().GetData())
  number_of_streamlines = polydata.GetLines().GetNumberOfCells()

  #
  # scalars are per point
  #
  pointdata = polydata.GetPointData()
  number_of_scalars = pointdata.GetNumberOfArrays()
  scalars = []
  scalar_types = []
  scalar_names = []

  for i in range(number_of_scalars):
      arr_name = pointdata.GetArrayName(i)
      scalar_names.append(str(arr_name))
      arr = pointdata.GetArray(i)

      # arr.ComputeScalarRange()

      # print(arr)

      number_of_components = arr.GetNumberOfComponents()
      data_type = arr.GetDataType()

      scalar_types.append((data_type, number_of_components))

      if verbose:
        print('Loading scalar', arr_name)
      scalars.append(numpy_support.vtk_to_numpy(arr))

  #
  # properties are per streamline
  #
  celldata = polydata.GetCellData()
  number_of_properties = celldata.GetNumberOfArrays()
  properties = []
  property_types = []
  property_names = []

  for i in range(number_of_properties):
      arr_name = celldata.GetArrayName(i)
      property_names.append(str(arr_name))
      arr = celldata.GetArray(i)

      # print(i, arr)

      number_of_components = arr.GetNumberOfComponents()
      data_type = arr.GetDataType()

      property_types.append((data_type, number_of_components))

      if verbose:
        print('Loading property', arr_name)
      properties.append(numpy_support.vtk_to_numpy(arr))


  #
  # convert to streamlines
  #
  ordered_indices = []
  ordered_scalars = []
  i = 0
  current_fiber_id = 0
  line_length = 0
  # sanity check
  if len(lines) > 0:
    line_length = lines[i]
  line_index = 0

  lines_just_length = []

  while (line_index<number_of_streamlines):

      lines_just_length.append(line_length)

      current_line = lines[i+1+line_index:i+1+line_length+line_index]
      current_indices = []

      # print('line',line_index)
      for k in range(len(current_line)-1):

          indexA = current_line[k]
          indexB = current_line[k+1]
      
          # print(indexA, indexB)
          current_indices.append(indexA)
          current_indices.append(indexB)
      
      ordered_indices += current_indices

      i += line_length
      line_index += 1
      if line_index < number_of_streamlines:
          line_length = lines[i+line_index]

  #
  # now, create fiber cluster data structure
  #
  fibercluster = {

    'number_of_streamlines': number_of_streamlines,
    'per_vertex_data': collections.OrderedDict(),
    'indices': lines_just_length, #ordered_indices
    'per_streamline_data': collections.OrderedDict()

  }

  fibercluster['per_vertex_data']['POSITION'] = {
    'componentType': vtkDataType_to_gltfComponentType[polydata.GetPoints().GetDataType()],
    'type': vtkNumberOfComponents_to_gltfType[polydata.GetPoints().GetData().GetNumberOfComponents()],
    'data': points#ordered_vertices
  }

  for i,s in enumerate(scalar_names):

    vtkdatatype = scalar_types[i][0]
    vtknumberofcomponents = scalar_types[i][1]

    thisdata = scalars[i]#[]

    if vtknumberofcomponents in vtkNumberOfComponents_to_gltfType:
      gltfType = vtkNumberOfComponents_to_gltfType[vtknumberofcomponents]
    else:
      # for now, we will just pass it through
      gltfType = vtknumberofcomponents

    fibercluster['per_vertex_data'][s] = {
      'componentType': vtkDataType_to_gltfComponentType[vtkdatatype],
      'type': gltfType,
      'data': thisdata
    }

  for i,p in enumerate(property_names):

    vtkdatatype = property_types[i][0]
    vtknumberofcomponents = property_types[i][1]

    thisdata = properties[i]#[]

    if vtknumberofcomponents in vtkNumberOfComponents_to_gltfType:
      gltfType = vtkNumberOfComponents_to_gltfType[vtknumberofcomponents]
    else:
      # for now, we will just pass it through
      gltfType = vtknumberofcomponents

    fibercluster['per_streamline_data'][p] = {
      'componentType': vtkDataType_to_gltfComponentType[vtkdatatype],
      'type': gltfType,
      'data': thisdata
    }

  return fibercluster


def fibercluster2gltf(fibercluster, draco=False, config=None, verbose=True):

  if config and draco:
    if verbose:
        print('Using custom configuration for Draco.')

  gltf = GLTF2()
  scene = Scene()
  scene.nodes.append(0)
  gltf.scene = 0
  gltf.scenes.append(scene)

  # we need a bunch of buffers for all the attributes
  buffers = collections.OrderedDict()
  for attributename in fibercluster['per_vertex_data'].keys():
    buffers[attributename] = Buffer()

  # and of course a bunch of chunkers per attribute
  chunkers = collections.OrderedDict()
  for attributename in fibercluster['per_vertex_data'].keys():
    chunkers[attributename] = b""

  # and a bunch of bufferviews
  bufferviews = []
  # and a bunch of accessors
  accessors = []

  # we need stuff for properties as well
  p_buffers = collections.OrderedDict()
  for p_name in fibercluster['per_streamline_data'].keys():
    p_buffers[p_name] = Buffer()
  p_chunkers = collections.OrderedDict()
  for p_name in fibercluster['per_streamline_data'].keys():
    p_chunkers[p_name] = b""

  # and a bunch of bufferviews
  p_bufferviews = []
  # and a bunch of accessors
  p_accessors = []

  node = Node() # one fiber cluster has a node
  mesh = Mesh() # .. and a mesh
  node.mesh = 0

  custom_attributes = {}
  custom_attribute_index = 0
  for attributename in fibercluster['per_vertex_data'].keys():
    if attributename != 'POSITION':
      # this is custom
      attributename = '_'+attributename
    custom_attributes[attributename] = custom_attribute_index
    custom_attribute_index += 1

  primitive = Primitive()
  for attributeindex,attributename in enumerate(custom_attributes.keys()):
    # we need to update the indices increasingly
    # print('before', s, custom_attributes[attributename])
    custom_attributes[attributename] = attributeindex
    # print('after', custom_attributes[attributename])

  primitive.attributes = Attributes(**custom_attributes)
  primitive.mode = 1


  for attributeindex,attributename in enumerate(fibercluster['per_vertex_data'].keys()):

    # if verbose:
    #     print('Parsing', attributename)

    componentType = fibercluster['per_vertex_data'][attributename]['componentType']
    aType = fibercluster['per_vertex_data'][attributename]['type']
    data = fibercluster['per_vertex_data'][attributename]['data']

    if componentType == pygltflib.FLOAT:
      asciiType = 'f'
      npType = float

    elif componentType == pygltflib.UNSIGNED_INT:
      asciiType = 'I'
      npType = int

    else:
      asciiType = 'f'
      npType = float
      if verbose:
        print('Type not supported!', componentType)

    if draco:

      # bounds = ([0],[0])
      # for index, values in enumerate(data):

      #   if not type(values) is np.ndarray:
      #     values = [values]

      #   if index == 0:
      #     # first loop run
      #     bounds = (list([float(v) for v in values]), list([float(v) for v in values]))
      #   else:
      #     for i,v in enumerate(values):       
      #       bounds[0][i] = min(float(bounds[0][i]), float(v))
      #       bounds[1][i] = max(float(bounds[1][i]), float(v))
      bounds = [[],[]]
      if data.ndim > 1:
        for k in range(data.shape[1]):
          bounds[0].append(npType(np.min(data[:,k])))
          bounds[1].append(npType(np.max(data[:,k])))
      else:
        bounds = [[npType(np.min(data))], [npType(np.max(data))]]
        

      if config:

        if attributename in config:

          position = config[attributename]['position']
          sequential = config[attributename]['sequential']
          qb = config[attributename]['quantization_bits']
          cl = config[attributename]['compression_level']
          qrange = config[attributename]['quantization_range']
          qorigin = config[attributename]['quantization_origin']

          if verbose:
            print ('Custom config for', attributename)

      else:

        # compress the chunks
        position = False
        if (attributename == 'POSITION'):
          position = True

        sequential = True
        qb=14
        cl=1
        qrange=-1
        qorigin=None

      # fix nan
      np.nan_to_num(data, copy=False)

      if data.shape[0] == 0:
        if verbose:
          print('Scalar with length 0! Skipping..')
        chunk = b""
      else:
        chunk = TrakoDracoPy.encode_point_cloud_to_buffer(data.ravel(), position=position, sequential=sequential, 
          quantization_bits=qb, compression_level=cl, quantization_range=qrange, quantization_origin=qorigin)

    else:

      bounds = [[],[]]
      if data.ndim > 1:
        for k in range(data.shape[1]):
          bounds[0].append(npType(np.min(data[:,k])))
          bounds[1].append(npType(np.max(data[:,k])))
      else:
        bounds = [[npType(np.min(data))], [npType(np.max(data))]]

      #
      # create bytestream for buffer
      #
      chunk = b""
      # bounds = (None, None) # min,max
      for index, values in enumerate(data):

        
        if not type(values) is np.ndarray:
          values = [values]

        # if chunk == b"":
        #   # first loop run
        #   bounds = (list([float(v) for v in values]), list([float(v) for v in values]))
        # else:
        #   for i,v in enumerate(values):       
        #     bounds[0][i] = min(float(bounds[0][i]), float(v))
        #     bounds[1][i] = max(float(bounds[1][i]), float(v))

        pack = "<" + (asciiType*len(values))

        subChunk = struct.pack(pack, *values)
        chunk += subChunk


    # each attribute has a bufferview for each streamline
    # and an accessor
    bufferview = BufferView()
    bufferview.target = ARRAY_BUFFER
    # print(buffers.keys())
    bufferview.buffer = attributeindex
    bufferview.byteOffset = 0#len(chunkers[attributename])##byteOffset 
    bufferview.byteLength = len(chunk) 
    bufferviews.append(bufferview)

    # print(len(chunkers[attributename]))

    chunkers[attributename] += chunk

    # byteOffset += len(chunk)


    accessor = Accessor()
    # print(accessor)
    accessor.bufferView = len(bufferviews)-1
    accessor.byteOffset = 0#byteOffset
    accessor.componentType = componentType
    accessor.count = len(data)
    accessor.type = aType
    accessor.min = list(bounds[0])
    accessor.max = list(bounds[1])
    accessors.append(accessor)

  # now indices
  indices = fibercluster['indices']

  if draco:

    # for index, values in enumerate(indices):

    #   values = [values]

    #   if chunk == b"":
    #     # first loop run
    #     bounds = (list([int(v) for v in values]), list([int(v) for v in values]))
    #   else:
    #     for i,v in enumerate(values):       
    #       bounds[0][i] = min(int(bounds[0][i]), int(v))
    #       bounds[1][i] = max(int(bounds[1][i]), int(v))

    # bounds = [[],[]]
    # if data.ndim > 1:
    #   for k in range(data.shape[1]):
    #     bounds[0].append(np.min(data[:,k]).astype(np.float))
    #     bounds[1].append(np.max(data[:,k]).astype(np.float))
    # else:
    bounds = [[int(np.min(indices))], [int(np.max(indices))]]


    if config:

      if 'INDICES' in config:

        attributename = 'INDICES'

        position = config[attributename]['position']
        sequential = config[attributename]['sequential']
        qb = config[attributename]['quantization_bits']
        cl = config[attributename]['compression_level']
        qrange = config[attributename]['quantization_range']
        qorigin = config[attributename]['quantization_origin']

        if verbose:
          print ('Custom config for', attributename)

    else:

      position = False
      sequential = True
      qb=14
      cl=1
      qrange=-1
      qorigin=None


    # fix nan
    np.nan_to_num(indices, copy=False)

    if len(indices) == 0:
      if verbose:
        print('Indices with length 0! Skipping..')
      i_chunk = b""
    else:
      i_chunk = TrakoDracoPy.encode_point_cloud_to_buffer(indices, position=False, sequential=True, 
        quantization_bits=qb, compression_level=cl, quantization_range=qrange, quantization_origin=qorigin)

  else:

    #
    # create bytestream for index buffer
    #
    i_chunk = b""
    # bounds = (None, None) # min,max
    bounds = [[int(np.min(indices))], [int(np.max(indices))]]

    for index, values in enumerate(indices):

      values = [values]

      # if i_chunk == b"":
      #   # first loop run
      #   bounds = (list([float(v) for v in values]), list([float(v) for v in values]))
      # else:
      #   for i,v in enumerate(values):       
      #     bounds[0][i] = min(int(bounds[0][i]), int(v))
      #     bounds[1][i] = max(int(bounds[1][i]), int(v))

      pack = "<" + ('H'*len(values))

      subChunk = struct.pack(pack, *values)
      i_chunk += subChunk


  bufferview = BufferView()
  bufferview.target = ELEMENT_ARRAY_BUFFER
  bufferview.buffer = attributeindex+1 # this is last buffer.. for now only -> properties below
  bufferview.byteOffset = 0
  bufferview.byteLength = len(chunk)

  # print(len(chunk), len(indices))

  primitive.indices = len(accessors) # again, NOT last one!

  accessor = Accessor()
  # print(accessor)
  accessor.bufferView = len(bufferviews) # the last buffer view
  accessor.byteOffset = 0#byteOffset
  accessor.componentType = UNSIGNED_SHORT
  accessor.count = len(indices)
  accessor.type = SCALAR
  accessor.min = list(bounds[0])
  accessor.max = list(bounds[1])


  #
  # properties
  # 
  properties = {} # this will later hold our accessor id's for the property data
  for p_index,p_name in enumerate(fibercluster['per_streamline_data'].keys()):

    componentType = fibercluster['per_streamline_data'][p_name]['componentType']
    aType = fibercluster['per_streamline_data'][p_name]['type']
    data = fibercluster['per_streamline_data'][p_name]['data']

    if componentType == pygltflib.FLOAT:
      asciiType = 'f'
      npType = float

    elif componentType == pygltflib.UNSIGNED_INT:
      asciiType = 'I'
      npType = int

    elif componentType == pygltflib.UNSIGNED_BYTE:
      asciiType = 'B'
      npType = int

    else:
      asciiType = 'f'
      npType = float
      print('Type not supported!', componentType)

    if draco:

      # print(data.shape)

      bounds = [[],[]]
      if data.ndim > 1:
        for k in range(data.shape[1]):
          bounds[0].append(npType(np.min(data[:,k])))
          bounds[1].append(npType(np.max(data[:,k])))
      else:
        bounds = [[npType(np.min(data))], [npType(np.max(data))]]
        

      # for index, values in enumerate(data):
      #   # print(index, values)

        
      #   if not type(values) is np.ndarray:
      #     values = [float(values)]

      #   if index == 0:
      #     # first loop run
      #     bounds = (list([float(v) for v in values]), list([float(v) for v in values]))
      #   else:
      #     for i,v in enumerate(values):       
      #       bounds[0][i] = min(float(bounds[0][i]), float(v))
      #       bounds[1][i] = max(float(bounds[1][i]), float(v))

      # print(bounds)
      # print(bounds2)

      if config:

        if p_name in config:

          position = config[p_name]['position']
          sequential = config[p_name]['sequential']
          qb = config[p_name]['quantization_bits']
          cl = config[p_name]['compression_level']
          qrange = config[p_name]['quantization_range']
          qorigin = config[p_name]['quantization_origin']

          if verbose:
            print ('Custom config for', p_name)

      else:

        # compress the chunks
        position = False
        sequential = True
        qb=14
        cl=1
        qrange=-1
        qorigin=None

      np.nan_to_num(data, copy=False)

      # print(data.shape)

      if data.shape[0] == 0:
        if verbose:
          print('Property with length 0! Skipping..')
        chunk = b""
      else:
        chunk = TrakoDracoPy.encode_point_cloud_to_buffer(data.ravel(), position=position, sequential=sequential, 
          quantization_bits=qb, compression_level=cl, quantization_range=qrange, quantization_origin=qorigin)

    else:

      #
      # create bytestream for buffer
      #
      bounds = [[],[]]
      if data.ndim > 1:
        for k in range(data.shape[1]):
          bounds[0].append(npType(np.min(data[:,k])))
          bounds[1].append(npType(np.max(data[:,k])))
      else:
        bounds = [[npType(np.min(data))], [npType(np.max(data))]]


      chunk = b""
      # bounds = (None, None) # min,max
      for index, values in enumerate(data):

        
        if not type(values) is np.ndarray:
          values = [values]

        # if chunk == b"":
        #   # first loop run
        #   bounds = (list([float(v) for v in values]), list([float(v) for v in values]))
        # else:
        #   for i,v in enumerate(values):       
        #     bounds[0][i] = min(float(bounds[0][i]), float(v))
        #     bounds[1][i] = max(float(bounds[1][i]), float(v))

        pack = "<" + (asciiType*len(values))

        subChunk = struct.pack(pack, *values)
        chunk += subChunk


    # we need bufferview
    # and an accessor
    p_bufferview = BufferView()
    p_bufferview.target = ARRAY_BUFFER
    # print(buffers.keys())
    p_bufferview.buffer = attributeindex+1+p_index+1 # first scalars, then indices, then properties
    p_bufferview.byteOffset = 0#len(chunkers[attributename])##byteOffset 
    p_bufferview.byteLength = len(chunk) 
    p_bufferviews.append(p_bufferview)

    # print(len(chunkers[attributename]))

    p_chunkers[p_name] += chunk

    # byteOffset += len(chunk)

    p_accessor = Accessor()
    # print(accessor)
    p_accessor.bufferView = len(bufferviews) + len(p_bufferviews)
    p_accessor.byteOffset = 0#byteOffset
    p_accessor.componentType = componentType
    p_accessor.count = len(data)
    p_accessor.type = aType
    p_accessor.min = list(bounds[0])
    p_accessor.max = list(bounds[1])
    p_accessors.append(p_accessor)


    properties[p_name] = len(accessors) + len(p_accessors)


  primitive.extras = {'properties': properties}

  # add this streamline to the mesh
  mesh.primitives.append(primitive)

  # now add the mesh to the scene
  gltf.meshes.append(mesh)
  gltf.nodes.append(node)

  # add the bufferviews and the accessors
  gltf.bufferViews += bufferviews + [bufferview] + p_bufferviews # per vertex, indices, per streamline
  gltf.accessors += accessors + [accessor] + p_accessors

  #
  # store all buffer data base64-encoded
  #
  for attributename in fibercluster['per_vertex_data'].keys():

    buffer = buffers[attributename]
    chunker = chunkers[attributename]

    buffer.uri = pygltflib.DATA_URI_HEADER
    buffer.uri += str(base64.b64encode(chunker), "utf-8")
    buffer.byteLength = len(chunker)

    gltf.buffers.append(buffer)


  # and now for the indices
  indexbuffer = Buffer()
  indexbuffer.uri = pygltflib.DATA_URI_HEADER
  indexbuffer.uri += str(base64.b64encode(i_chunk), "utf-8")
  indexbuffer.byteLength = len(i_chunk)
  gltf.buffers.append(indexbuffer)

  # and now for the properties
  for p_name in fibercluster['per_streamline_data'].keys():

    buffer = p_buffers[p_name]
    chunker = p_chunkers[p_name]

    buffer.uri = pygltflib.DATA_URI_HEADER
    buffer.uri += str(base64.b64encode(chunker), "utf-8")
    buffer.byteLength = len(chunker)

    gltf.buffers.append(buffer)


  return gltf

