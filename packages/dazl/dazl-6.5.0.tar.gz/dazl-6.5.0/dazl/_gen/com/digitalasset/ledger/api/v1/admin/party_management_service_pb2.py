# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/ledger/api/v1/admin/party_management_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/digitalasset/ledger/api/v1/admin/party_management_service.proto',
  package='com.digitalasset.ledger.api.v1.admin',
  syntax='proto3',
  serialized_options=_b('\n$com.digitalasset.ledger.api.v1.adminB PartyManagementServiceOuterClass\252\002$Com.DigitalAsset.Ledger.Api.V1.Admin'),
  serialized_pb=_b('\nCcom/digitalasset/ledger/api/v1/admin/party_management_service.proto\x12$com.digitalasset.ledger.api.v1.admin\"\x19\n\x17GetParticipantIdRequest\"2\n\x18GetParticipantIdResponse\x12\x16\n\x0eparticipant_id\x18\x01 \x01(\t\"\x19\n\x17ListKnownPartiesRequest\"e\n\x18ListKnownPartiesResponse\x12I\n\rparty_details\x18\x01 \x03(\x0b\x32\x32.com.digitalasset.ledger.api.v1.admin.PartyDetails\"E\n\x0cPartyDetails\x12\r\n\x05party\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x10\n\x08is_local\x18\x03 \x01(\x08\"C\n\x14\x41llocatePartyRequest\x12\x15\n\rparty_id_hint\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\"b\n\x15\x41llocatePartyResponse\x12I\n\rparty_details\x18\x01 \x01(\x0b\x32\x32.com.digitalasset.ledger.api.v1.admin.PartyDetails2\xcb\x03\n\x16PartyManagementService\x12\x91\x01\n\x10GetParticipantId\x12=.com.digitalasset.ledger.api.v1.admin.GetParticipantIdRequest\x1a>.com.digitalasset.ledger.api.v1.admin.GetParticipantIdResponse\x12\x91\x01\n\x10ListKnownParties\x12=.com.digitalasset.ledger.api.v1.admin.ListKnownPartiesRequest\x1a>.com.digitalasset.ledger.api.v1.admin.ListKnownPartiesResponse\x12\x88\x01\n\rAllocateParty\x12:.com.digitalasset.ledger.api.v1.admin.AllocatePartyRequest\x1a;.com.digitalasset.ledger.api.v1.admin.AllocatePartyResponseBo\n$com.digitalasset.ledger.api.v1.adminB PartyManagementServiceOuterClass\xaa\x02$Com.DigitalAsset.Ledger.Api.V1.Adminb\x06proto3')
)




_GETPARTICIPANTIDREQUEST = _descriptor.Descriptor(
  name='GetParticipantIdRequest',
  full_name='com.digitalasset.ledger.api.v1.admin.GetParticipantIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=109,
  serialized_end=134,
)


_GETPARTICIPANTIDRESPONSE = _descriptor.Descriptor(
  name='GetParticipantIdResponse',
  full_name='com.digitalasset.ledger.api.v1.admin.GetParticipantIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='participant_id', full_name='com.digitalasset.ledger.api.v1.admin.GetParticipantIdResponse.participant_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=136,
  serialized_end=186,
)


_LISTKNOWNPARTIESREQUEST = _descriptor.Descriptor(
  name='ListKnownPartiesRequest',
  full_name='com.digitalasset.ledger.api.v1.admin.ListKnownPartiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=188,
  serialized_end=213,
)


_LISTKNOWNPARTIESRESPONSE = _descriptor.Descriptor(
  name='ListKnownPartiesResponse',
  full_name='com.digitalasset.ledger.api.v1.admin.ListKnownPartiesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='party_details', full_name='com.digitalasset.ledger.api.v1.admin.ListKnownPartiesResponse.party_details', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=215,
  serialized_end=316,
)


_PARTYDETAILS = _descriptor.Descriptor(
  name='PartyDetails',
  full_name='com.digitalasset.ledger.api.v1.admin.PartyDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='party', full_name='com.digitalasset.ledger.api.v1.admin.PartyDetails.party', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='com.digitalasset.ledger.api.v1.admin.PartyDetails.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_local', full_name='com.digitalasset.ledger.api.v1.admin.PartyDetails.is_local', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=318,
  serialized_end=387,
)


_ALLOCATEPARTYREQUEST = _descriptor.Descriptor(
  name='AllocatePartyRequest',
  full_name='com.digitalasset.ledger.api.v1.admin.AllocatePartyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='party_id_hint', full_name='com.digitalasset.ledger.api.v1.admin.AllocatePartyRequest.party_id_hint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='com.digitalasset.ledger.api.v1.admin.AllocatePartyRequest.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=389,
  serialized_end=456,
)


_ALLOCATEPARTYRESPONSE = _descriptor.Descriptor(
  name='AllocatePartyResponse',
  full_name='com.digitalasset.ledger.api.v1.admin.AllocatePartyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='party_details', full_name='com.digitalasset.ledger.api.v1.admin.AllocatePartyResponse.party_details', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=458,
  serialized_end=556,
)

_LISTKNOWNPARTIESRESPONSE.fields_by_name['party_details'].message_type = _PARTYDETAILS
_ALLOCATEPARTYRESPONSE.fields_by_name['party_details'].message_type = _PARTYDETAILS
DESCRIPTOR.message_types_by_name['GetParticipantIdRequest'] = _GETPARTICIPANTIDREQUEST
DESCRIPTOR.message_types_by_name['GetParticipantIdResponse'] = _GETPARTICIPANTIDRESPONSE
DESCRIPTOR.message_types_by_name['ListKnownPartiesRequest'] = _LISTKNOWNPARTIESREQUEST
DESCRIPTOR.message_types_by_name['ListKnownPartiesResponse'] = _LISTKNOWNPARTIESRESPONSE
DESCRIPTOR.message_types_by_name['PartyDetails'] = _PARTYDETAILS
DESCRIPTOR.message_types_by_name['AllocatePartyRequest'] = _ALLOCATEPARTYREQUEST
DESCRIPTOR.message_types_by_name['AllocatePartyResponse'] = _ALLOCATEPARTYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetParticipantIdRequest = _reflection.GeneratedProtocolMessageType('GetParticipantIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPARTICIPANTIDREQUEST,
  '__module__' : 'com.digitalasset.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.admin.GetParticipantIdRequest)
  })
_sym_db.RegisterMessage(GetParticipantIdRequest)

GetParticipantIdResponse = _reflection.GeneratedProtocolMessageType('GetParticipantIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPARTICIPANTIDRESPONSE,
  '__module__' : 'com.digitalasset.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.admin.GetParticipantIdResponse)
  })
_sym_db.RegisterMessage(GetParticipantIdResponse)

ListKnownPartiesRequest = _reflection.GeneratedProtocolMessageType('ListKnownPartiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTKNOWNPARTIESREQUEST,
  '__module__' : 'com.digitalasset.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.admin.ListKnownPartiesRequest)
  })
_sym_db.RegisterMessage(ListKnownPartiesRequest)

ListKnownPartiesResponse = _reflection.GeneratedProtocolMessageType('ListKnownPartiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTKNOWNPARTIESRESPONSE,
  '__module__' : 'com.digitalasset.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.admin.ListKnownPartiesResponse)
  })
_sym_db.RegisterMessage(ListKnownPartiesResponse)

PartyDetails = _reflection.GeneratedProtocolMessageType('PartyDetails', (_message.Message,), {
  'DESCRIPTOR' : _PARTYDETAILS,
  '__module__' : 'com.digitalasset.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.admin.PartyDetails)
  })
_sym_db.RegisterMessage(PartyDetails)

AllocatePartyRequest = _reflection.GeneratedProtocolMessageType('AllocatePartyRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEPARTYREQUEST,
  '__module__' : 'com.digitalasset.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.admin.AllocatePartyRequest)
  })
_sym_db.RegisterMessage(AllocatePartyRequest)

AllocatePartyResponse = _reflection.GeneratedProtocolMessageType('AllocatePartyResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEPARTYRESPONSE,
  '__module__' : 'com.digitalasset.ledger.api.v1.admin.party_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.admin.AllocatePartyResponse)
  })
_sym_db.RegisterMessage(AllocatePartyResponse)


DESCRIPTOR._options = None

_PARTYMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='PartyManagementService',
  full_name='com.digitalasset.ledger.api.v1.admin.PartyManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=559,
  serialized_end=1018,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetParticipantId',
    full_name='com.digitalasset.ledger.api.v1.admin.PartyManagementService.GetParticipantId',
    index=0,
    containing_service=None,
    input_type=_GETPARTICIPANTIDREQUEST,
    output_type=_GETPARTICIPANTIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListKnownParties',
    full_name='com.digitalasset.ledger.api.v1.admin.PartyManagementService.ListKnownParties',
    index=1,
    containing_service=None,
    input_type=_LISTKNOWNPARTIESREQUEST,
    output_type=_LISTKNOWNPARTIESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AllocateParty',
    full_name='com.digitalasset.ledger.api.v1.admin.PartyManagementService.AllocateParty',
    index=2,
    containing_service=None,
    input_type=_ALLOCATEPARTYREQUEST,
    output_type=_ALLOCATEPARTYRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PARTYMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['PartyManagementService'] = _PARTYMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)
