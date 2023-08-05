# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import ledger_identity_service_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2


class LedgerIdentityServiceStub(object):
  """Allows clients to verify that the server they are communicating with exposes the ledger they wish to operate on.
  Note that every ledger has a unique ID.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLedgerIdentity = channel.unary_unary(
        '/com.digitalasset.ledger.api.v1.LedgerIdentityService/GetLedgerIdentity',
        request_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityRequest.SerializeToString,
        response_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityResponse.FromString,
        )


class LedgerIdentityServiceServicer(object):
  """Allows clients to verify that the server they are communicating with exposes the ledger they wish to operate on.
  Note that every ledger has a unique ID.
  """

  def GetLedgerIdentity(self, request, context):
    """Clients may call this RPC to return the identifier of the ledger they are connected to.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LedgerIdentityServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLedgerIdentity': grpc.unary_unary_rpc_method_handler(
          servicer.GetLedgerIdentity,
          request_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityRequest.FromString,
          response_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_ledger__identity__service__pb2.GetLedgerIdentityResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.digitalasset.ledger.api.v1.LedgerIdentityService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
