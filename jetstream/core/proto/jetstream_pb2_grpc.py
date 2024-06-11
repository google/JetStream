# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
# pylint: disable=all
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from jetstream.core.proto import jetstream_pb2 as jetstream_dot_core_dot_proto_dot_jetstream__pb2


class OrchestratorStub(object):
  """TODO: Merge this with main JetStream core once we settle on an API."""

  def __init__(self, channel):
    """Constructor.

    Args:
        channel: A grpc.Channel.
    """
    self.Decode = channel.unary_stream(
        "/jetstream_proto.Orchestrator/Decode",
        request_serializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.DecodeRequest.SerializeToString,
        response_deserializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.DecodeResponse.FromString,
    )
    self.HealthCheck = channel.unary_unary(
        "/jetstream_proto.Orchestrator/HealthCheck",
        request_serializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.HealthCheckRequest.SerializeToString,
        response_deserializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.HealthCheckResponse.FromString,
    )


class OrchestratorServicer(object):
  """TODO: Merge this with main JetStream core once we settle on an API."""

  def Decode(self, request, context):
    """Query LLM to generate text or tokens."""
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details("Method not implemented!")
    raise NotImplementedError("Method not implemented!")

  def HealthCheck(self, request, context):
    """Checks if the model server is live."""
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details("Method not implemented!")
    raise NotImplementedError("Method not implemented!")


def add_OrchestratorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      "Decode": grpc.unary_stream_rpc_method_handler(
          servicer.Decode,
          request_deserializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.DecodeRequest.FromString,
          response_serializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.DecodeResponse.SerializeToString,
      ),
      "HealthCheck": grpc.unary_unary_rpc_method_handler(
          servicer.HealthCheck,
          request_deserializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.HealthCheckRequest.FromString,
          response_serializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.HealthCheckResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      "jetstream_proto.Orchestrator", rpc_method_handlers
  )
  server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Orchestrator(object):
  """TODO: Merge this with main JetStream core once we settle on an API."""

  @staticmethod
  def Decode(
      request,
      target,
      options=(),
      channel_credentials=None,
      call_credentials=None,
      insecure=False,
      compression=None,
      wait_for_ready=None,
      timeout=None,
      metadata=None,
  ):
    return grpc.experimental.unary_stream(
        request,
        target,
        "/jetstream_proto.Orchestrator/Decode",
        jetstream_dot_core_dot_proto_dot_jetstream__pb2.DecodeRequest.SerializeToString,
        jetstream_dot_core_dot_proto_dot_jetstream__pb2.DecodeResponse.FromString,
        options,
        channel_credentials,
        insecure,
        call_credentials,
        compression,
        wait_for_ready,
        timeout,
        metadata,
    )

  @staticmethod
  def HealthCheck(
      request,
      target,
      options=(),
      channel_credentials=None,
      call_credentials=None,
      insecure=False,
      compression=None,
      wait_for_ready=None,
      timeout=None,
      metadata=None,
  ):
    return grpc.experimental.unary_unary(
        request,
        target,
        "/jetstream_proto.Orchestrator/HealthCheck",
        jetstream_dot_core_dot_proto_dot_jetstream__pb2.HealthCheckRequest.SerializeToString,
        jetstream_dot_core_dot_proto_dot_jetstream__pb2.HealthCheckResponse.FromString,
        options,
        channel_credentials,
        insecure,
        call_credentials,
        compression,
        wait_for_ready,
        timeout,
        metadata,
    )


class UtilitiesStub(object):
  """Utility RPCs for JetStream"""

  def __init__(self, channel):
    """Constructor.

    Args:
        channel: A grpc.Channel.
    """
    self.ModelWarmup = channel.unary_unary(
        "/jetstream_proto.Utilities/ModelWarmup",
        request_serializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.ModelWarmupRequest.SerializeToString,
        response_deserializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.ModelWarmupResponse.FromString,
    )


class UtilitiesServicer(object):
  """Utility RPCs for JetStream"""

  def ModelWarmup(self, request, context):
    """Warms up the model server."""
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details("Method not implemented!")
    raise NotImplementedError("Method not implemented!")


def add_UtilitiesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      "ModelWarmup": grpc.unary_unary_rpc_method_handler(
          servicer.ModelWarmup,
          request_deserializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.ModelWarmupRequest.FromString,
          response_serializer=jetstream_dot_core_dot_proto_dot_jetstream__pb2.ModelWarmupResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      "jetstream_proto.Utilities", rpc_method_handlers
  )
  server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Utilities(object):
  """Utility RPCs for JetStream"""

  @staticmethod
  def ModelWarmup(
      request,
      target,
      options=(),
      channel_credentials=None,
      call_credentials=None,
      insecure=False,
      compression=None,
      wait_for_ready=None,
      timeout=None,
      metadata=None,
  ):
    return grpc.experimental.unary_unary(
        request,
        target,
        "/jetstream_proto.Utilities/ModelWarmup",
        jetstream_dot_core_dot_proto_dot_jetstream__pb2.ModelWarmupRequest.SerializeToString,
        jetstream_dot_core_dot_proto_dot_jetstream__pb2.ModelWarmupResponse.FromString,
        options,
        channel_credentials,
        insecure,
        call_credentials,
        compression,
        wait_for_ready,
        timeout,
        metadata,
    )
