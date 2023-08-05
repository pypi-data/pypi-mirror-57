# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/uploader/proto/export_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tensorboard.compat.proto import summary_pb2 as tensorboard_dot_compat_dot_proto_dot_summary__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/uploader/proto/export_service.proto',
  package='tensorboard.service',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/tensorboard/uploader/proto/export_service.proto\x12\x13tensorboard.service\x1a\x1fgoogle/protobuf/timestamp.proto\x1a&tensorboard/compat/proto/summary.proto\"\xad\x01\n\x18StreamExperimentsRequest\x12\x32\n\x0eread_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x03\x12=\n\x10\x65xperiments_mask\x18\x04 \x01(\x0b\x32#.tensorboard.service.ExperimentMask\"i\n\x19StreamExperimentsResponse\x12\x16\n\x0e\x65xperiment_ids\x18\x01 \x03(\t\x12\x34\n\x0b\x65xperiments\x18\x02 \x03(\x0b\x32\x1f.tensorboard.service.Experiment\"\xbe\x01\n\nExperiment\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\x12/\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bnum_scalars\x18\x04 \x01(\x03\x12\x10\n\x08num_runs\x18\x05 \x01(\x03\x12\x10\n\x08num_tags\x18\x06 \x01(\x03\"\x88\x01\n\x0e\x45xperimentMask\x12\x13\n\x0b\x63reate_time\x18\x02 \x01(\x08\x12\x13\n\x0bupdate_time\x18\x03 \x01(\x08\x12\x13\n\x0bnum_scalars\x18\x04 \x01(\x08\x12\x10\n\x08num_runs\x18\x05 \x01(\x08\x12\x10\n\x08num_tags\x18\x06 \x01(\x08J\x04\x08\x01\x10\x02R\rexperiment_id\"h\n\x1bStreamExperimentDataRequest\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\x12\x32\n\x0eread_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa5\x02\n\x1cStreamExperimentDataResponse\x12\x10\n\x08tag_name\x18\x01 \x01(\t\x12\x10\n\x08run_name\x18\x02 \x01(\t\x12\x32\n\x0ctag_metadata\x18\x03 \x01(\x0b\x32\x1c.tensorboard.SummaryMetadata\x12N\n\x06points\x18\x04 \x01(\x0b\x32>.tensorboard.service.StreamExperimentDataResponse.ScalarPoints\x1a]\n\x0cScalarPoints\x12\r\n\x05steps\x18\x01 \x03(\x03\x12.\n\nwall_times\x18\x02 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06values\x18\x03 \x03(\x01\x32\x95\x02\n\x1aTensorBoardExporterService\x12v\n\x11StreamExperiments\x12-.tensorboard.service.StreamExperimentsRequest\x1a..tensorboard.service.StreamExperimentsResponse\"\x00\x30\x01\x12\x7f\n\x14StreamExperimentData\x12\x30.tensorboard.service.StreamExperimentDataRequest\x1a\x31.tensorboard.service.StreamExperimentDataResponse\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,tensorboard_dot_compat_dot_proto_dot_summary__pb2.DESCRIPTOR,])




_STREAMEXPERIMENTSREQUEST = _descriptor.Descriptor(
  name='StreamExperimentsRequest',
  full_name='tensorboard.service.StreamExperimentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='read_timestamp', full_name='tensorboard.service.StreamExperimentsRequest.read_timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tensorboard.service.StreamExperimentsRequest.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='tensorboard.service.StreamExperimentsRequest.limit', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiments_mask', full_name='tensorboard.service.StreamExperimentsRequest.experiments_mask', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=146,
  serialized_end=319,
)


_STREAMEXPERIMENTSRESPONSE = _descriptor.Descriptor(
  name='StreamExperimentsResponse',
  full_name='tensorboard.service.StreamExperimentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_ids', full_name='tensorboard.service.StreamExperimentsResponse.experiment_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiments', full_name='tensorboard.service.StreamExperimentsResponse.experiments', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=321,
  serialized_end=426,
)


_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='tensorboard.service.Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='tensorboard.service.Experiment.experiment_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='tensorboard.service.Experiment.create_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='tensorboard.service.Experiment.update_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_scalars', full_name='tensorboard.service.Experiment.num_scalars', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_runs', full_name='tensorboard.service.Experiment.num_runs', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_tags', full_name='tensorboard.service.Experiment.num_tags', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=429,
  serialized_end=619,
)


_EXPERIMENTMASK = _descriptor.Descriptor(
  name='ExperimentMask',
  full_name='tensorboard.service.ExperimentMask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create_time', full_name='tensorboard.service.ExperimentMask.create_time', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='tensorboard.service.ExperimentMask.update_time', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_scalars', full_name='tensorboard.service.ExperimentMask.num_scalars', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_runs', full_name='tensorboard.service.ExperimentMask.num_runs', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_tags', full_name='tensorboard.service.ExperimentMask.num_tags', index=4,
      number=6, type=8, cpp_type=7, label=1,
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
  serialized_start=622,
  serialized_end=758,
)


_STREAMEXPERIMENTDATAREQUEST = _descriptor.Descriptor(
  name='StreamExperimentDataRequest',
  full_name='tensorboard.service.StreamExperimentDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='tensorboard.service.StreamExperimentDataRequest.experiment_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_timestamp', full_name='tensorboard.service.StreamExperimentDataRequest.read_timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=760,
  serialized_end=864,
)


_STREAMEXPERIMENTDATARESPONSE_SCALARPOINTS = _descriptor.Descriptor(
  name='ScalarPoints',
  full_name='tensorboard.service.StreamExperimentDataResponse.ScalarPoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steps', full_name='tensorboard.service.StreamExperimentDataResponse.ScalarPoints.steps', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wall_times', full_name='tensorboard.service.StreamExperimentDataResponse.ScalarPoints.wall_times', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='tensorboard.service.StreamExperimentDataResponse.ScalarPoints.values', index=2,
      number=3, type=1, cpp_type=5, label=3,
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
  serialized_start=1067,
  serialized_end=1160,
)

_STREAMEXPERIMENTDATARESPONSE = _descriptor.Descriptor(
  name='StreamExperimentDataResponse',
  full_name='tensorboard.service.StreamExperimentDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag_name', full_name='tensorboard.service.StreamExperimentDataResponse.tag_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_name', full_name='tensorboard.service.StreamExperimentDataResponse.run_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_metadata', full_name='tensorboard.service.StreamExperimentDataResponse.tag_metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='tensorboard.service.StreamExperimentDataResponse.points', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STREAMEXPERIMENTDATARESPONSE_SCALARPOINTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=867,
  serialized_end=1160,
)

_STREAMEXPERIMENTSREQUEST.fields_by_name['read_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STREAMEXPERIMENTSREQUEST.fields_by_name['experiments_mask'].message_type = _EXPERIMENTMASK
_STREAMEXPERIMENTSRESPONSE.fields_by_name['experiments'].message_type = _EXPERIMENT
_EXPERIMENT.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXPERIMENT.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STREAMEXPERIMENTDATAREQUEST.fields_by_name['read_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STREAMEXPERIMENTDATARESPONSE_SCALARPOINTS.fields_by_name['wall_times'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STREAMEXPERIMENTDATARESPONSE_SCALARPOINTS.containing_type = _STREAMEXPERIMENTDATARESPONSE
_STREAMEXPERIMENTDATARESPONSE.fields_by_name['tag_metadata'].message_type = tensorboard_dot_compat_dot_proto_dot_summary__pb2._SUMMARYMETADATA
_STREAMEXPERIMENTDATARESPONSE.fields_by_name['points'].message_type = _STREAMEXPERIMENTDATARESPONSE_SCALARPOINTS
DESCRIPTOR.message_types_by_name['StreamExperimentsRequest'] = _STREAMEXPERIMENTSREQUEST
DESCRIPTOR.message_types_by_name['StreamExperimentsResponse'] = _STREAMEXPERIMENTSRESPONSE
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
DESCRIPTOR.message_types_by_name['ExperimentMask'] = _EXPERIMENTMASK
DESCRIPTOR.message_types_by_name['StreamExperimentDataRequest'] = _STREAMEXPERIMENTDATAREQUEST
DESCRIPTOR.message_types_by_name['StreamExperimentDataResponse'] = _STREAMEXPERIMENTDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamExperimentsRequest = _reflection.GeneratedProtocolMessageType('StreamExperimentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMEXPERIMENTSREQUEST,
  '__module__' : 'tensorboard.uploader.proto.export_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.StreamExperimentsRequest)
  })
_sym_db.RegisterMessage(StreamExperimentsRequest)

StreamExperimentsResponse = _reflection.GeneratedProtocolMessageType('StreamExperimentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMEXPERIMENTSRESPONSE,
  '__module__' : 'tensorboard.uploader.proto.export_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.StreamExperimentsResponse)
  })
_sym_db.RegisterMessage(StreamExperimentsResponse)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENT,
  '__module__' : 'tensorboard.uploader.proto.export_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.Experiment)
  })
_sym_db.RegisterMessage(Experiment)

ExperimentMask = _reflection.GeneratedProtocolMessageType('ExperimentMask', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTMASK,
  '__module__' : 'tensorboard.uploader.proto.export_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.ExperimentMask)
  })
_sym_db.RegisterMessage(ExperimentMask)

StreamExperimentDataRequest = _reflection.GeneratedProtocolMessageType('StreamExperimentDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMEXPERIMENTDATAREQUEST,
  '__module__' : 'tensorboard.uploader.proto.export_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.StreamExperimentDataRequest)
  })
_sym_db.RegisterMessage(StreamExperimentDataRequest)

StreamExperimentDataResponse = _reflection.GeneratedProtocolMessageType('StreamExperimentDataResponse', (_message.Message,), {

  'ScalarPoints' : _reflection.GeneratedProtocolMessageType('ScalarPoints', (_message.Message,), {
    'DESCRIPTOR' : _STREAMEXPERIMENTDATARESPONSE_SCALARPOINTS,
    '__module__' : 'tensorboard.uploader.proto.export_service_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.service.StreamExperimentDataResponse.ScalarPoints)
    })
  ,
  'DESCRIPTOR' : _STREAMEXPERIMENTDATARESPONSE,
  '__module__' : 'tensorboard.uploader.proto.export_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.StreamExperimentDataResponse)
  })
_sym_db.RegisterMessage(StreamExperimentDataResponse)
_sym_db.RegisterMessage(StreamExperimentDataResponse.ScalarPoints)



_TENSORBOARDEXPORTERSERVICE = _descriptor.ServiceDescriptor(
  name='TensorBoardExporterService',
  full_name='tensorboard.service.TensorBoardExporterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1163,
  serialized_end=1440,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamExperiments',
    full_name='tensorboard.service.TensorBoardExporterService.StreamExperiments',
    index=0,
    containing_service=None,
    input_type=_STREAMEXPERIMENTSREQUEST,
    output_type=_STREAMEXPERIMENTSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamExperimentData',
    full_name='tensorboard.service.TensorBoardExporterService.StreamExperimentData',
    index=1,
    containing_service=None,
    input_type=_STREAMEXPERIMENTDATAREQUEST,
    output_type=_STREAMEXPERIMENTDATARESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TENSORBOARDEXPORTERSERVICE)

DESCRIPTOR.services_by_name['TensorBoardExporterService'] = _TENSORBOARDEXPORTERSERVICE

# @@protoc_insertion_point(module_scope)
