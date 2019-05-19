# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/protos/ydb_issue_message.proto

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
  name='kikimr/public/api/protos/ydb_issue_message.proto',
  package='Ydb.Issue',
  syntax='proto2',
  serialized_pb=_b('\n0kikimr/public/api/protos/ydb_issue_message.proto\x12\tYdb.Issue\"\x91\x02\n\x0cIssueMessage\x12\x32\n\x08position\x18\x01 \x01(\x0b\x32 .Ydb.Issue.IssueMessage.Position\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x36\n\x0c\x65nd_position\x18\x03 \x01(\x0b\x32 .Ydb.Issue.IssueMessage.Position\x12\x12\n\nissue_code\x18\x04 \x01(\r\x12\x10\n\x08severity\x18\x05 \x01(\r\x12\'\n\x06issues\x18\x06 \x03(\x0b\x32\x17.Ydb.Issue.IssueMessage\x1a\x35\n\x08Position\x12\x0b\n\x03row\x18\x01 \x01(\r\x12\x0e\n\x06\x63olumn\x18\x02 \x01(\r\x12\x0c\n\x04\x66ile\x18\x03 \x01(\tB\x10\n\x0e\x63om.yandex.ydb')
)




_ISSUEMESSAGE_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='Ydb.Issue.IssueMessage.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='Ydb.Issue.IssueMessage.Position.row', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='column', full_name='Ydb.Issue.IssueMessage.Position.column', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file', full_name='Ydb.Issue.IssueMessage.Position.file', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=284,
  serialized_end=337,
)

_ISSUEMESSAGE = _descriptor.Descriptor(
  name='IssueMessage',
  full_name='Ydb.Issue.IssueMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='Ydb.Issue.IssueMessage.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='Ydb.Issue.IssueMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_position', full_name='Ydb.Issue.IssueMessage.end_position', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='issue_code', full_name='Ydb.Issue.IssueMessage.issue_code', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='Ydb.Issue.IssueMessage.severity', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='issues', full_name='Ydb.Issue.IssueMessage.issues', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ISSUEMESSAGE_POSITION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=337,
)

_ISSUEMESSAGE_POSITION.containing_type = _ISSUEMESSAGE
_ISSUEMESSAGE.fields_by_name['position'].message_type = _ISSUEMESSAGE_POSITION
_ISSUEMESSAGE.fields_by_name['end_position'].message_type = _ISSUEMESSAGE_POSITION
_ISSUEMESSAGE.fields_by_name['issues'].message_type = _ISSUEMESSAGE
DESCRIPTOR.message_types_by_name['IssueMessage'] = _ISSUEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IssueMessage = _reflection.GeneratedProtocolMessageType('IssueMessage', (_message.Message,), dict(

  Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
    DESCRIPTOR = _ISSUEMESSAGE_POSITION,
    __module__ = 'kikimr.public.api.protos.ydb_issue_message_pb2'
    # @@protoc_insertion_point(class_scope:Ydb.Issue.IssueMessage.Position)
    ))
  ,
  DESCRIPTOR = _ISSUEMESSAGE,
  __module__ = 'kikimr.public.api.protos.ydb_issue_message_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Issue.IssueMessage)
  ))
_sym_db.RegisterMessage(IssueMessage)
_sym_db.RegisterMessage(IssueMessage.Position)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016com.yandex.ydb'))
# @@protoc_insertion_point(module_scope)
