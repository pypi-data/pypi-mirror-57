# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/ledger/api/v1/ledger_offset.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/digitalasset/ledger/api/v1/ledger_offset.proto',
  package='com.digitalasset.ledger.api.v1',
  syntax='proto3',
  serialized_options=_b('\n\036com.digitalasset.ledger.api.v1B\026LedgerOffsetOuterClass\252\002\036Com.DigitalAsset.Ledger.Api.V1'),
  serialized_pb=_b('\n2com/digitalasset/ledger/api/v1/ledger_offset.proto\x12\x1e\x63om.digitalasset.ledger.api.v1\"\xb0\x01\n\x0cLedgerOffset\x12\x12\n\x08\x61\x62solute\x18\x01 \x01(\tH\x00\x12O\n\x08\x62oundary\x18\x02 \x01(\x0e\x32;.com.digitalasset.ledger.api.v1.LedgerOffset.LedgerBoundaryH\x00\"2\n\x0eLedgerBoundary\x12\x10\n\x0cLEDGER_BEGIN\x10\x00\x12\x0e\n\nLEDGER_END\x10\x01\x42\x07\n\x05valueBY\n\x1e\x63om.digitalasset.ledger.api.v1B\x16LedgerOffsetOuterClass\xaa\x02\x1e\x43om.DigitalAsset.Ledger.Api.V1b\x06proto3')
)



_LEDGEROFFSET_LEDGERBOUNDARY = _descriptor.EnumDescriptor(
  name='LedgerBoundary',
  full_name='com.digitalasset.ledger.api.v1.LedgerOffset.LedgerBoundary',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEDGER_BEGIN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEDGER_END', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=204,
  serialized_end=254,
)
_sym_db.RegisterEnumDescriptor(_LEDGEROFFSET_LEDGERBOUNDARY)


_LEDGEROFFSET = _descriptor.Descriptor(
  name='LedgerOffset',
  full_name='com.digitalasset.ledger.api.v1.LedgerOffset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='absolute', full_name='com.digitalasset.ledger.api.v1.LedgerOffset.absolute', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boundary', full_name='com.digitalasset.ledger.api.v1.LedgerOffset.boundary', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEDGEROFFSET_LEDGERBOUNDARY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='com.digitalasset.ledger.api.v1.LedgerOffset.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=87,
  serialized_end=263,
)

_LEDGEROFFSET.fields_by_name['boundary'].enum_type = _LEDGEROFFSET_LEDGERBOUNDARY
_LEDGEROFFSET_LEDGERBOUNDARY.containing_type = _LEDGEROFFSET
_LEDGEROFFSET.oneofs_by_name['value'].fields.append(
  _LEDGEROFFSET.fields_by_name['absolute'])
_LEDGEROFFSET.fields_by_name['absolute'].containing_oneof = _LEDGEROFFSET.oneofs_by_name['value']
_LEDGEROFFSET.oneofs_by_name['value'].fields.append(
  _LEDGEROFFSET.fields_by_name['boundary'])
_LEDGEROFFSET.fields_by_name['boundary'].containing_oneof = _LEDGEROFFSET.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['LedgerOffset'] = _LEDGEROFFSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LedgerOffset = _reflection.GeneratedProtocolMessageType('LedgerOffset', (_message.Message,), {
  'DESCRIPTOR' : _LEDGEROFFSET,
  '__module__' : 'com.digitalasset.ledger.api.v1.ledger_offset_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.LedgerOffset)
  })
_sym_db.RegisterMessage(LedgerOffset)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
