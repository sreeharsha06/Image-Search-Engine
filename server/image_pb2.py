# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11proto/image.proto\"\x1f\n\x0cImageRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"\x1e\n\rImageResponse\x12\r\n\x05image\x18\x01 \x01(\x0c\x32;\n\x0bImageSearch\x12,\n\x0bsearchImage\x12\r.ImageRequest\x1a\x0e.ImageResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.image_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_IMAGEREQUEST']._serialized_start=21
  _globals['_IMAGEREQUEST']._serialized_end=52
  _globals['_IMAGERESPONSE']._serialized_start=54
  _globals['_IMAGERESPONSE']._serialized_end=84
  _globals['_IMAGESEARCH']._serialized_start=86
  _globals['_IMAGESEARCH']._serialized_end=145
# @@protoc_insertion_point(module_scope)
