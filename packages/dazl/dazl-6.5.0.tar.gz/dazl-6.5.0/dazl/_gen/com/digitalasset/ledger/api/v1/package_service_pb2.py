# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/ledger/api/v1/package_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import trace_context_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/digitalasset/ledger/api/v1/package_service.proto',
  package='com.digitalasset.ledger.api.v1',
  syntax='proto3',
  serialized_options=_b('\n\036com.digitalasset.ledger.api.v1B\030PackageServiceOuterClass\252\002\036Com.DigitalAsset.Ledger.Api.V1'),
  serialized_pb=_b('\n4com/digitalasset/ledger/api/v1/package_service.proto\x12\x1e\x63om.digitalasset.ledger.api.v1\x1a\x32\x63om/digitalasset/ledger/api/v1/trace_context.proto\"n\n\x13ListPackagesRequest\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x44\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32,.com.digitalasset.ledger.api.v1.TraceContext\"+\n\x14ListPackagesResponse\x12\x13\n\x0bpackage_ids\x18\x01 \x03(\t\"\x80\x01\n\x11GetPackageRequest\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x12\n\npackage_id\x18\x02 \x01(\t\x12\x44\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32,.com.digitalasset.ledger.api.v1.TraceContext\"\x80\x01\n\x12GetPackageResponse\x12\x43\n\rhash_function\x18\x01 \x01(\x0e\x32,.com.digitalasset.ledger.api.v1.HashFunction\x12\x17\n\x0f\x61rchive_payload\x18\x02 \x01(\x0c\x12\x0c\n\x04hash\x18\x03 \x01(\t\"\x86\x01\n\x17GetPackageStatusRequest\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x12\n\npackage_id\x18\x02 \x01(\t\x12\x44\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32,.com.digitalasset.ledger.api.v1.TraceContext\"a\n\x18GetPackageStatusResponse\x12\x45\n\x0epackage_status\x18\x01 \x01(\x0e\x32-.com.digitalasset.ledger.api.v1.PackageStatus*,\n\rPackageStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nREGISTERED\x10\x01*\x1a\n\x0cHashFunction\x12\n\n\x06SHA256\x10\x00\x32\x88\x03\n\x0ePackageService\x12y\n\x0cListPackages\x12\x33.com.digitalasset.ledger.api.v1.ListPackagesRequest\x1a\x34.com.digitalasset.ledger.api.v1.ListPackagesResponse\x12s\n\nGetPackage\x12\x31.com.digitalasset.ledger.api.v1.GetPackageRequest\x1a\x32.com.digitalasset.ledger.api.v1.GetPackageResponse\x12\x85\x01\n\x10GetPackageStatus\x12\x37.com.digitalasset.ledger.api.v1.GetPackageStatusRequest\x1a\x38.com.digitalasset.ledger.api.v1.GetPackageStatusResponseB[\n\x1e\x63om.digitalasset.ledger.api.v1B\x18PackageServiceOuterClass\xaa\x02\x1e\x43om.DigitalAsset.Ledger.Api.V1b\x06proto3')
  ,
  dependencies=[com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2.DESCRIPTOR,])

_PACKAGESTATUS = _descriptor.EnumDescriptor(
  name='PackageStatus',
  full_name='com.digitalasset.ledger.api.v1.PackageStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTERED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=795,
  serialized_end=839,
)
_sym_db.RegisterEnumDescriptor(_PACKAGESTATUS)

PackageStatus = enum_type_wrapper.EnumTypeWrapper(_PACKAGESTATUS)
_HASHFUNCTION = _descriptor.EnumDescriptor(
  name='HashFunction',
  full_name='com.digitalasset.ledger.api.v1.HashFunction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SHA256', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=841,
  serialized_end=867,
)
_sym_db.RegisterEnumDescriptor(_HASHFUNCTION)

HashFunction = enum_type_wrapper.EnumTypeWrapper(_HASHFUNCTION)
UNKNOWN = 0
REGISTERED = 1
SHA256 = 0



_LISTPACKAGESREQUEST = _descriptor.Descriptor(
  name='ListPackagesRequest',
  full_name='com.digitalasset.ledger.api.v1.ListPackagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.digitalasset.ledger.api.v1.ListPackagesRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.digitalasset.ledger.api.v1.ListPackagesRequest.trace_context', index=1,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=250,
)


_LISTPACKAGESRESPONSE = _descriptor.Descriptor(
  name='ListPackagesResponse',
  full_name='com.digitalasset.ledger.api.v1.ListPackagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_ids', full_name='com.digitalasset.ledger.api.v1.ListPackagesResponse.package_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=295,
)


_GETPACKAGEREQUEST = _descriptor.Descriptor(
  name='GetPackageRequest',
  full_name='com.digitalasset.ledger.api.v1.GetPackageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.digitalasset.ledger.api.v1.GetPackageRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_id', full_name='com.digitalasset.ledger.api.v1.GetPackageRequest.package_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.digitalasset.ledger.api.v1.GetPackageRequest.trace_context', index=2,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=426,
)


_GETPACKAGERESPONSE = _descriptor.Descriptor(
  name='GetPackageResponse',
  full_name='com.digitalasset.ledger.api.v1.GetPackageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash_function', full_name='com.digitalasset.ledger.api.v1.GetPackageResponse.hash_function', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='archive_payload', full_name='com.digitalasset.ledger.api.v1.GetPackageResponse.archive_payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='com.digitalasset.ledger.api.v1.GetPackageResponse.hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=557,
)


_GETPACKAGESTATUSREQUEST = _descriptor.Descriptor(
  name='GetPackageStatusRequest',
  full_name='com.digitalasset.ledger.api.v1.GetPackageStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.digitalasset.ledger.api.v1.GetPackageStatusRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_id', full_name='com.digitalasset.ledger.api.v1.GetPackageStatusRequest.package_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.digitalasset.ledger.api.v1.GetPackageStatusRequest.trace_context', index=2,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=560,
  serialized_end=694,
)


_GETPACKAGESTATUSRESPONSE = _descriptor.Descriptor(
  name='GetPackageStatusResponse',
  full_name='com.digitalasset.ledger.api.v1.GetPackageStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_status', full_name='com.digitalasset.ledger.api.v1.GetPackageStatusResponse.package_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=793,
)

_LISTPACKAGESREQUEST.fields_by_name['trace_context'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_GETPACKAGEREQUEST.fields_by_name['trace_context'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_GETPACKAGERESPONSE.fields_by_name['hash_function'].enum_type = _HASHFUNCTION
_GETPACKAGESTATUSREQUEST.fields_by_name['trace_context'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_GETPACKAGESTATUSRESPONSE.fields_by_name['package_status'].enum_type = _PACKAGESTATUS
DESCRIPTOR.message_types_by_name['ListPackagesRequest'] = _LISTPACKAGESREQUEST
DESCRIPTOR.message_types_by_name['ListPackagesResponse'] = _LISTPACKAGESRESPONSE
DESCRIPTOR.message_types_by_name['GetPackageRequest'] = _GETPACKAGEREQUEST
DESCRIPTOR.message_types_by_name['GetPackageResponse'] = _GETPACKAGERESPONSE
DESCRIPTOR.message_types_by_name['GetPackageStatusRequest'] = _GETPACKAGESTATUSREQUEST
DESCRIPTOR.message_types_by_name['GetPackageStatusResponse'] = _GETPACKAGESTATUSRESPONSE
DESCRIPTOR.enum_types_by_name['PackageStatus'] = _PACKAGESTATUS
DESCRIPTOR.enum_types_by_name['HashFunction'] = _HASHFUNCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListPackagesRequest = _reflection.GeneratedProtocolMessageType('ListPackagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPACKAGESREQUEST,
  '__module__' : 'com.digitalasset.ledger.api.v1.package_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.ListPackagesRequest)
  })
_sym_db.RegisterMessage(ListPackagesRequest)

ListPackagesResponse = _reflection.GeneratedProtocolMessageType('ListPackagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPACKAGESRESPONSE,
  '__module__' : 'com.digitalasset.ledger.api.v1.package_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.ListPackagesResponse)
  })
_sym_db.RegisterMessage(ListPackagesResponse)

GetPackageRequest = _reflection.GeneratedProtocolMessageType('GetPackageRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPACKAGEREQUEST,
  '__module__' : 'com.digitalasset.ledger.api.v1.package_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.GetPackageRequest)
  })
_sym_db.RegisterMessage(GetPackageRequest)

GetPackageResponse = _reflection.GeneratedProtocolMessageType('GetPackageResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPACKAGERESPONSE,
  '__module__' : 'com.digitalasset.ledger.api.v1.package_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.GetPackageResponse)
  })
_sym_db.RegisterMessage(GetPackageResponse)

GetPackageStatusRequest = _reflection.GeneratedProtocolMessageType('GetPackageStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPACKAGESTATUSREQUEST,
  '__module__' : 'com.digitalasset.ledger.api.v1.package_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.GetPackageStatusRequest)
  })
_sym_db.RegisterMessage(GetPackageStatusRequest)

GetPackageStatusResponse = _reflection.GeneratedProtocolMessageType('GetPackageStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPACKAGESTATUSRESPONSE,
  '__module__' : 'com.digitalasset.ledger.api.v1.package_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.GetPackageStatusResponse)
  })
_sym_db.RegisterMessage(GetPackageStatusResponse)


DESCRIPTOR._options = None

_PACKAGESERVICE = _descriptor.ServiceDescriptor(
  name='PackageService',
  full_name='com.digitalasset.ledger.api.v1.PackageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=870,
  serialized_end=1262,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListPackages',
    full_name='com.digitalasset.ledger.api.v1.PackageService.ListPackages',
    index=0,
    containing_service=None,
    input_type=_LISTPACKAGESREQUEST,
    output_type=_LISTPACKAGESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPackage',
    full_name='com.digitalasset.ledger.api.v1.PackageService.GetPackage',
    index=1,
    containing_service=None,
    input_type=_GETPACKAGEREQUEST,
    output_type=_GETPACKAGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPackageStatus',
    full_name='com.digitalasset.ledger.api.v1.PackageService.GetPackageStatus',
    index=2,
    containing_service=None,
    input_type=_GETPACKAGESTATUSREQUEST,
    output_type=_GETPACKAGESTATUSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PACKAGESERVICE)

DESCRIPTOR.services_by_name['PackageService'] = _PACKAGESERVICE

# @@protoc_insertion_point(module_scope)
