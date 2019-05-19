# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/ydb_discovery_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_discovery_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__discovery__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/ydb_discovery_v1.proto',
  package='Ydb.Discovery.V1',
  syntax='proto3',
  serialized_pb=_b('\n-kikimr/public/api/grpc/ydb_discovery_v1.proto\x12\x10Ydb.Discovery.V1\x1a,kikimr/public/api/protos/ydb_discovery.proto2n\n\x10\x44iscoveryService\x12Z\n\rListEndpoints\x12#.Ydb.Discovery.ListEndpointsRequest\x1a$.Ydb.Discovery.ListEndpointsResponseB\x1d\n\x1b\x63om.yandex.ydb.discovery.v1b\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__discovery__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033com.yandex.ydb.discovery.v1'))

_DISCOVERYSERVICE = _descriptor.ServiceDescriptor(
  name='DiscoveryService',
  full_name='Ydb.Discovery.V1.DiscoveryService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=113,
  serialized_end=223,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListEndpoints',
    full_name='Ydb.Discovery.V1.DiscoveryService.ListEndpoints',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__discovery__pb2._LISTENDPOINTSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__discovery__pb2._LISTENDPOINTSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISCOVERYSERVICE)

DESCRIPTOR.services_by_name['DiscoveryService'] = _DISCOVERYSERVICE

# @@protoc_insertion_point(module_scope)
