# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RegisterFaceIdWithPicParams.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RegisterFaceIdWithPicParams.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n!RegisterFaceIdWithPicParams.proto\"A\n\x1bRegisterFaceIdWithPicParams\x12\x10\n\x08\x66\x61\x63\x65Name\x18\x01 \x02(\t\x12\x10\n\x08\x66ilePath\x18\x02 \x02(\t\"E\n\x1eRegisterFaceIdFromCameraParams\x12\x10\n\x08\x66\x61\x63\x65Name\x18\x01 \x02(\t\x12\x11\n\ttimeoutMs\x18\x02 \x02(\x05\"3\n\x0fSetFaceIdParams\x12\x0e\n\x06\x66\x61\x63\x65Id\x18\x01 \x02(\x05\x12\x10\n\x08\x66\x61\x63\x65Name\x18\x02 \x02(\t\"1\n\x10ListFaceIdParams\x12\r\n\x05start\x18\x01 \x02(\x05\x12\x0e\n\x06length\x18\x02 \x02(\x05\".\n\nFaceIdInfo\x12\x0e\n\x06\x66\x61\x63\x65Id\x18\x01 \x02(\x05\x12\x10\n\x08\x66\x61\x63\x65Name\x18\x02 \x02(\t\";\n\x0e\x46\x61\x63\x65IdListData\x12\r\n\x05start\x18\x01 \x02(\x05\x12\x1a\n\x05\x66\x61\x63\x65s\x18\x02 \x03(\x0b\x32\x0b.FaceIdInfo')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REGISTERFACEIDWITHPICPARAMS = _descriptor.Descriptor(
  name='RegisterFaceIdWithPicParams',
  full_name='RegisterFaceIdWithPicParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faceName', full_name='RegisterFaceIdWithPicParams.faceName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filePath', full_name='RegisterFaceIdWithPicParams.filePath', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=102,
)


_REGISTERFACEIDFROMCAMERAPARAMS = _descriptor.Descriptor(
  name='RegisterFaceIdFromCameraParams',
  full_name='RegisterFaceIdFromCameraParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faceName', full_name='RegisterFaceIdFromCameraParams.faceName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeoutMs', full_name='RegisterFaceIdFromCameraParams.timeoutMs', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=173,
)


_SETFACEIDPARAMS = _descriptor.Descriptor(
  name='SetFaceIdParams',
  full_name='SetFaceIdParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faceId', full_name='SetFaceIdParams.faceId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='faceName', full_name='SetFaceIdParams.faceName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=226,
)


_LISTFACEIDPARAMS = _descriptor.Descriptor(
  name='ListFaceIdParams',
  full_name='ListFaceIdParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ListFaceIdParams.start', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='ListFaceIdParams.length', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=228,
  serialized_end=277,
)


_FACEIDINFO = _descriptor.Descriptor(
  name='FaceIdInfo',
  full_name='FaceIdInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faceId', full_name='FaceIdInfo.faceId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='faceName', full_name='FaceIdInfo.faceName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=279,
  serialized_end=325,
)


_FACEIDLISTDATA = _descriptor.Descriptor(
  name='FaceIdListData',
  full_name='FaceIdListData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='FaceIdListData.start', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='faces', full_name='FaceIdListData.faces', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=386,
)

_FACEIDLISTDATA.fields_by_name['faces'].message_type = _FACEIDINFO
DESCRIPTOR.message_types_by_name['RegisterFaceIdWithPicParams'] = _REGISTERFACEIDWITHPICPARAMS
DESCRIPTOR.message_types_by_name['RegisterFaceIdFromCameraParams'] = _REGISTERFACEIDFROMCAMERAPARAMS
DESCRIPTOR.message_types_by_name['SetFaceIdParams'] = _SETFACEIDPARAMS
DESCRIPTOR.message_types_by_name['ListFaceIdParams'] = _LISTFACEIDPARAMS
DESCRIPTOR.message_types_by_name['FaceIdInfo'] = _FACEIDINFO
DESCRIPTOR.message_types_by_name['FaceIdListData'] = _FACEIDLISTDATA

RegisterFaceIdWithPicParams = _reflection.GeneratedProtocolMessageType('RegisterFaceIdWithPicParams', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERFACEIDWITHPICPARAMS,
  __module__ = 'RegisterFaceIdWithPicParams_pb2'
  # @@protoc_insertion_point(class_scope:RegisterFaceIdWithPicParams)
  ))
_sym_db.RegisterMessage(RegisterFaceIdWithPicParams)

RegisterFaceIdFromCameraParams = _reflection.GeneratedProtocolMessageType('RegisterFaceIdFromCameraParams', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERFACEIDFROMCAMERAPARAMS,
  __module__ = 'RegisterFaceIdWithPicParams_pb2'
  # @@protoc_insertion_point(class_scope:RegisterFaceIdFromCameraParams)
  ))
_sym_db.RegisterMessage(RegisterFaceIdFromCameraParams)

SetFaceIdParams = _reflection.GeneratedProtocolMessageType('SetFaceIdParams', (_message.Message,), dict(
  DESCRIPTOR = _SETFACEIDPARAMS,
  __module__ = 'RegisterFaceIdWithPicParams_pb2'
  # @@protoc_insertion_point(class_scope:SetFaceIdParams)
  ))
_sym_db.RegisterMessage(SetFaceIdParams)

ListFaceIdParams = _reflection.GeneratedProtocolMessageType('ListFaceIdParams', (_message.Message,), dict(
  DESCRIPTOR = _LISTFACEIDPARAMS,
  __module__ = 'RegisterFaceIdWithPicParams_pb2'
  # @@protoc_insertion_point(class_scope:ListFaceIdParams)
  ))
_sym_db.RegisterMessage(ListFaceIdParams)

FaceIdInfo = _reflection.GeneratedProtocolMessageType('FaceIdInfo', (_message.Message,), dict(
  DESCRIPTOR = _FACEIDINFO,
  __module__ = 'RegisterFaceIdWithPicParams_pb2'
  # @@protoc_insertion_point(class_scope:FaceIdInfo)
  ))
_sym_db.RegisterMessage(FaceIdInfo)

FaceIdListData = _reflection.GeneratedProtocolMessageType('FaceIdListData', (_message.Message,), dict(
  DESCRIPTOR = _FACEIDLISTDATA,
  __module__ = 'RegisterFaceIdWithPicParams_pb2'
  # @@protoc_insertion_point(class_scope:FaceIdListData)
  ))
_sym_db.RegisterMessage(FaceIdListData)


# @@protoc_insertion_point(module_scope)
