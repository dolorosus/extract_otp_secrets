# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: google_auth.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'google_auth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11google_auth.proto\"\xb7\x03\n\x10MigrationPayload\x12\x37\n\x0eotp_parameters\x18\x01 \x03(\x0b\x32\x1f.MigrationPayload.OtpParameters\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x12\n\nbatch_size\x18\x03 \x01(\x05\x12\x13\n\x0b\x62\x61tch_index\x18\x04 \x01(\x05\x12\x10\n\x08\x62\x61tch_id\x18\x05 \x01(\x05\x1a\xb7\x01\n\rOtpParameters\x12\x0e\n\x06secret\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06issuer\x18\x03 \x01(\t\x12.\n\talgorithm\x18\x04 \x01(\x0e\x32\x1b.MigrationPayload.Algorithm\x12\x0e\n\x06\x64igits\x18\x05 \x01(\x05\x12\'\n\x04type\x18\x06 \x01(\x0e\x32\x19.MigrationPayload.OtpType\x12\x0f\n\x07\x63ounter\x18\x07 \x01(\x03\",\n\tAlgorithm\x12\x10\n\x0c\x41LGO_INVALID\x10\x00\x12\r\n\tALGO_SHA1\x10\x01\"6\n\x07OtpType\x12\x0f\n\x0bOTP_INVALID\x10\x00\x12\x0c\n\x08OTP_HOTP\x10\x01\x12\x0c\n\x08OTP_TOTP\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google_auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MIGRATIONPAYLOAD']._serialized_start=22
  _globals['_MIGRATIONPAYLOAD']._serialized_end=461
  _globals['_MIGRATIONPAYLOAD_OTPPARAMETERS']._serialized_start=176
  _globals['_MIGRATIONPAYLOAD_OTPPARAMETERS']._serialized_end=359
  _globals['_MIGRATIONPAYLOAD_ALGORITHM']._serialized_start=361
  _globals['_MIGRATIONPAYLOAD_ALGORITHM']._serialized_end=405
  _globals['_MIGRATIONPAYLOAD_OTPTYPE']._serialized_start=407
  _globals['_MIGRATIONPAYLOAD_OTPTYPE']._serialized_end=461
# @@protoc_insertion_point(module_scope)
