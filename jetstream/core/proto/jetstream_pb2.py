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

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jetstream/core/proto/jetstream.proto
# Protobuf Python Version: 4.25.1
# pylint: disable=all
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n$jetstream/core/proto/jetstream.proto\x12\x0fjetstream_proto"\xa7\x02\n\rDecodeRequest\x12\x15\n\rsession_cache\x18\x01 \x01(\t\x12\x10\n\x08priority\x18\x03 \x01(\x05\x12\x12\n\nmax_tokens\x18\x04 \x01(\x05\x12\x42\n\x0ctext_content\x18\x05 \x01(\x0b\x32*.jetstream_proto.DecodeRequest.TextContentH\x00\x12\x44\n\rtoken_content\x18\x06 \x01(\x0b\x32+.jetstream_proto.DecodeRequest.TokenContentH\x00\x1a\x1b\n\x0bTextContent\x12\x0c\n\x04text\x18\x01 \x01(\t\x1a!\n\x0cTokenContent\x12\x11\n\ttoken_ids\x18\x01 \x03(\x05\x42\t\n\x07\x63ontentJ\x04\x08\x02\x10\x03"\xcb\x02\n\x0e\x44\x65\x63odeResponse\x12I\n\x0finitial_content\x18\x02 \x01(\x0b\x32..jetstream_proto.DecodeResponse.InitialContentH\x00\x12G\n\x0estream_content\x18\x03 \x01(\x0b\x32-.jetstream_proto.DecodeResponse.StreamContentH\x00\x1a\x10\n\x0eInitialContent\x1a\x81\x01\n\rStreamContent\x12\x45\n\x07samples\x18\x01 \x03(\x0b\x32\x34.jetstream_proto.DecodeResponse.StreamContent.Sample\x1a)\n\x06Sample\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x11\n\ttoken_ids\x18\x02 \x03(\x05\x42\t\n\x07\x63ontentJ\x04\x08\x01\x10\x02"\x14\n\x12HealthCheckRequest"&\n\x13HealthCheckResponse\x12\x0f\n\x07is_live\x18\x01 \x01(\x08"$\n\x12ModelWarmupRequest\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08"-\n\x13ModelWarmupResponse\x12\x16\n\x0ewarmup_enabled\x18\x01 \x01(\x08\x32\xb9\x01\n\x0cOrchestrator\x12M\n\x06\x44\x65\x63ode\x12\x1e.jetstream_proto.DecodeRequest\x1a\x1f.jetstream_proto.DecodeResponse"\x00\x30\x01\x12Z\n\x0bHealthCheck\x12#.jetstream_proto.HealthCheckRequest\x1a$.jetstream_proto.HealthCheckResponse"\x00\x32g\n\tUtilities\x12Z\n\x0bModelWarmup\x12#.jetstream_proto.ModelWarmupRequest\x1a$.jetstream_proto.ModelWarmupResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "jetstream.core.proto.jetstream_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals["_DECODEREQUEST"]._serialized_start = 58
  _globals["_DECODEREQUEST"]._serialized_end = 353
  _globals["_DECODEREQUEST_TEXTCONTENT"]._serialized_start = 274
  _globals["_DECODEREQUEST_TEXTCONTENT"]._serialized_end = 301
  _globals["_DECODEREQUEST_TOKENCONTENT"]._serialized_start = 303
  _globals["_DECODEREQUEST_TOKENCONTENT"]._serialized_end = 336
  _globals["_DECODERESPONSE"]._serialized_start = 356
  _globals["_DECODERESPONSE"]._serialized_end = 687
  _globals["_DECODERESPONSE_INITIALCONTENT"]._serialized_start = 522
  _globals["_DECODERESPONSE_INITIALCONTENT"]._serialized_end = 538
  _globals["_DECODERESPONSE_STREAMCONTENT"]._serialized_start = 541
  _globals["_DECODERESPONSE_STREAMCONTENT"]._serialized_end = 670
  _globals["_DECODERESPONSE_STREAMCONTENT_SAMPLE"]._serialized_start = 629
  _globals["_DECODERESPONSE_STREAMCONTENT_SAMPLE"]._serialized_end = 670
  _globals["_HEALTHCHECKREQUEST"]._serialized_start = 689
  _globals["_HEALTHCHECKREQUEST"]._serialized_end = 709
  _globals["_HEALTHCHECKRESPONSE"]._serialized_start = 711
  _globals["_HEALTHCHECKRESPONSE"]._serialized_end = 749
  _globals["_MODELWARMUPREQUEST"]._serialized_start = 751
  _globals["_MODELWARMUPREQUEST"]._serialized_end = 787
  _globals["_MODELWARMUPRESPONSE"]._serialized_start = 789
  _globals["_MODELWARMUPRESPONSE"]._serialized_end = 834
  _globals["_ORCHESTRATOR"]._serialized_start = 837
  _globals["_ORCHESTRATOR"]._serialized_end = 1022
  _globals["_UTILITIES"]._serialized_start = 1024
  _globals["_UTILITIES"]._serialized_end = 1127
# @@protoc_insertion_point(module_scope)
