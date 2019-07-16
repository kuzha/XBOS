# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: baseline_optimizer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='baseline_optimizer.proto',
  package='baseline_optimizer',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x18\x62\x61seline_optimizer.proto\x12\x12\x62\x61seline_optimizer\"\xbd\x02\n\x15NormalScheduleRequest\x12\x10\n\x08\x62uilding\x18\x01 \x01(\t\x12\r\n\x05zones\x18\x02 \x03(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x03\x12\x0e\n\x06window\x18\x05 \x01(\t\x12\x62\n\x15starting_temperatures\x18\x06 \x03(\x0b\x32\x43.baseline_optimizer.NormalScheduleRequest.StartingTemperaturesEntry\x12\x0c\n\x04unit\x18\x07 \x01(\t\x12\x11\n\toccupancy\x18\x08 \x01(\x08\x12\x15\n\rdo_not_exceed\x18\t \x01(\x08\x1a;\n\x19StartingTemperaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\xdb\x03\n\x18SetpointExpansionRequest\x12\x10\n\x08\x62uilding\x18\x01 \x01(\t\x12\r\n\x05zones\x18\x02 \x03(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x03\x12\x0e\n\x06window\x18\x05 \x01(\t\x12\x65\n\x15starting_temperatures\x18\x06 \x03(\x0b\x32\x46.baseline_optimizer.SetpointExpansionRequest.StartingTemperaturesEntry\x12]\n\x11\x65xpansion_degrees\x18\x07 \x03(\x0b\x32\x42.baseline_optimizer.SetpointExpansionRequest.ExpansionDegreesEntry\x12\x0c\n\x04unit\x18\x08 \x01(\t\x12\x11\n\toccupancy\x18\t \x01(\x08\x12\x15\n\rdo_not_exceed\x18\n \x01(\x08\x1a;\n\x19StartingTemperaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x37\n\x15\x45xpansionDegreesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\xe7\x02\n\x13\x44\x65mandChargeRequest\x12\x10\n\x08\x62uilding\x18\x01 \x01(\t\x12\r\n\x05zones\x18\x02 \x03(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x03\x12\x0e\n\x06window\x18\x05 \x01(\t\x12`\n\x15starting_temperatures\x18\x06 \x03(\x0b\x32\x41.baseline_optimizer.DemandChargeRequest.StartingTemperaturesEntry\x12\x0c\n\x04unit\x18\x07 \x01(\t\x12\x11\n\tmax_zones\x18\x08 \x01(\x03\x12\x19\n\x11include_all_zones\x18\t \x01(\x08\x12\x11\n\toccupancy\x18\n \x01(\x08\x12\x15\n\rdo_not_exceed\x18\x0b \x01(\x08\x1a;\n\x19StartingTemperaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"p\n\x05Reply\x12\x37\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32&.baseline_optimizer.Reply.ActionsEntry\x1a.\n\x0c\x41\x63tionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x32\xfb\x04\n\x11\x42\x61selineOptimizer\x12\x61\n\x17GetNormalScheduleAction\x12).baseline_optimizer.NormalScheduleRequest\x1a\x19.baseline_optimizer.Reply\"\x00\x12g\n\x1aGetSetpointExpansionAction\x12,.baseline_optimizer.SetpointExpansionRequest\x1a\x19.baseline_optimizer.Reply\"\x00\x12]\n\x15GetDemandChargeAction\x12\'.baseline_optimizer.DemandChargeRequest\x1a\x19.baseline_optimizer.Reply\"\x00\x12g\n\x1bGetNormalScheduleSimulation\x12).baseline_optimizer.NormalScheduleRequest\x1a\x19.baseline_optimizer.Reply\"\x00\x30\x01\x12m\n\x1eGetSetpointExpansionSimulation\x12,.baseline_optimizer.SetpointExpansionRequest\x1a\x19.baseline_optimizer.Reply\"\x00\x30\x01\x12\x63\n\x19GetDemandChargeSimualtion\x12\'.baseline_optimizer.DemandChargeRequest\x1a\x19.baseline_optimizer.Reply\"\x00\x30\x01\x42\x02P\x01\x62\x06proto3')
)




_NORMALSCHEDULEREQUEST_STARTINGTEMPERATURESENTRY = _descriptor.Descriptor(
  name='StartingTemperaturesEntry',
  full_name='baseline_optimizer.NormalScheduleRequest.StartingTemperaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='baseline_optimizer.NormalScheduleRequest.StartingTemperaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='baseline_optimizer.NormalScheduleRequest.StartingTemperaturesEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=366,
)

_NORMALSCHEDULEREQUEST = _descriptor.Descriptor(
  name='NormalScheduleRequest',
  full_name='baseline_optimizer.NormalScheduleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building', full_name='baseline_optimizer.NormalScheduleRequest.building', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zones', full_name='baseline_optimizer.NormalScheduleRequest.zones', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='baseline_optimizer.NormalScheduleRequest.start', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='baseline_optimizer.NormalScheduleRequest.end', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window', full_name='baseline_optimizer.NormalScheduleRequest.window', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starting_temperatures', full_name='baseline_optimizer.NormalScheduleRequest.starting_temperatures', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='baseline_optimizer.NormalScheduleRequest.unit', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occupancy', full_name='baseline_optimizer.NormalScheduleRequest.occupancy', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_not_exceed', full_name='baseline_optimizer.NormalScheduleRequest.do_not_exceed', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NORMALSCHEDULEREQUEST_STARTINGTEMPERATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=366,
)


_SETPOINTEXPANSIONREQUEST_STARTINGTEMPERATURESENTRY = _descriptor.Descriptor(
  name='StartingTemperaturesEntry',
  full_name='baseline_optimizer.SetpointExpansionRequest.StartingTemperaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='baseline_optimizer.SetpointExpansionRequest.StartingTemperaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='baseline_optimizer.SetpointExpansionRequest.StartingTemperaturesEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=366,
)

_SETPOINTEXPANSIONREQUEST_EXPANSIONDEGREESENTRY = _descriptor.Descriptor(
  name='ExpansionDegreesEntry',
  full_name='baseline_optimizer.SetpointExpansionRequest.ExpansionDegreesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='baseline_optimizer.SetpointExpansionRequest.ExpansionDegreesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='baseline_optimizer.SetpointExpansionRequest.ExpansionDegreesEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=789,
  serialized_end=844,
)

_SETPOINTEXPANSIONREQUEST = _descriptor.Descriptor(
  name='SetpointExpansionRequest',
  full_name='baseline_optimizer.SetpointExpansionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building', full_name='baseline_optimizer.SetpointExpansionRequest.building', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zones', full_name='baseline_optimizer.SetpointExpansionRequest.zones', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='baseline_optimizer.SetpointExpansionRequest.start', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='baseline_optimizer.SetpointExpansionRequest.end', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window', full_name='baseline_optimizer.SetpointExpansionRequest.window', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starting_temperatures', full_name='baseline_optimizer.SetpointExpansionRequest.starting_temperatures', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expansion_degrees', full_name='baseline_optimizer.SetpointExpansionRequest.expansion_degrees', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='baseline_optimizer.SetpointExpansionRequest.unit', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occupancy', full_name='baseline_optimizer.SetpointExpansionRequest.occupancy', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_not_exceed', full_name='baseline_optimizer.SetpointExpansionRequest.do_not_exceed', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SETPOINTEXPANSIONREQUEST_STARTINGTEMPERATURESENTRY, _SETPOINTEXPANSIONREQUEST_EXPANSIONDEGREESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=844,
)


_DEMANDCHARGEREQUEST_STARTINGTEMPERATURESENTRY = _descriptor.Descriptor(
  name='StartingTemperaturesEntry',
  full_name='baseline_optimizer.DemandChargeRequest.StartingTemperaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='baseline_optimizer.DemandChargeRequest.StartingTemperaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='baseline_optimizer.DemandChargeRequest.StartingTemperaturesEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=366,
)

_DEMANDCHARGEREQUEST = _descriptor.Descriptor(
  name='DemandChargeRequest',
  full_name='baseline_optimizer.DemandChargeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building', full_name='baseline_optimizer.DemandChargeRequest.building', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zones', full_name='baseline_optimizer.DemandChargeRequest.zones', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='baseline_optimizer.DemandChargeRequest.start', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='baseline_optimizer.DemandChargeRequest.end', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window', full_name='baseline_optimizer.DemandChargeRequest.window', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starting_temperatures', full_name='baseline_optimizer.DemandChargeRequest.starting_temperatures', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='baseline_optimizer.DemandChargeRequest.unit', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_zones', full_name='baseline_optimizer.DemandChargeRequest.max_zones', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='include_all_zones', full_name='baseline_optimizer.DemandChargeRequest.include_all_zones', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occupancy', full_name='baseline_optimizer.DemandChargeRequest.occupancy', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_not_exceed', full_name='baseline_optimizer.DemandChargeRequest.do_not_exceed', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEMANDCHARGEREQUEST_STARTINGTEMPERATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=847,
  serialized_end=1206,
)


_REPLY_ACTIONSENTRY = _descriptor.Descriptor(
  name='ActionsEntry',
  full_name='baseline_optimizer.Reply.ActionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='baseline_optimizer.Reply.ActionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='baseline_optimizer.Reply.ActionsEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1274,
  serialized_end=1320,
)

_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='baseline_optimizer.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actions', full_name='baseline_optimizer.Reply.actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REPLY_ACTIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1208,
  serialized_end=1320,
)

_NORMALSCHEDULEREQUEST_STARTINGTEMPERATURESENTRY.containing_type = _NORMALSCHEDULEREQUEST
_NORMALSCHEDULEREQUEST.fields_by_name['starting_temperatures'].message_type = _NORMALSCHEDULEREQUEST_STARTINGTEMPERATURESENTRY
_SETPOINTEXPANSIONREQUEST_STARTINGTEMPERATURESENTRY.containing_type = _SETPOINTEXPANSIONREQUEST
_SETPOINTEXPANSIONREQUEST_EXPANSIONDEGREESENTRY.containing_type = _SETPOINTEXPANSIONREQUEST
_SETPOINTEXPANSIONREQUEST.fields_by_name['starting_temperatures'].message_type = _SETPOINTEXPANSIONREQUEST_STARTINGTEMPERATURESENTRY
_SETPOINTEXPANSIONREQUEST.fields_by_name['expansion_degrees'].message_type = _SETPOINTEXPANSIONREQUEST_EXPANSIONDEGREESENTRY
_DEMANDCHARGEREQUEST_STARTINGTEMPERATURESENTRY.containing_type = _DEMANDCHARGEREQUEST
_DEMANDCHARGEREQUEST.fields_by_name['starting_temperatures'].message_type = _DEMANDCHARGEREQUEST_STARTINGTEMPERATURESENTRY
_REPLY_ACTIONSENTRY.containing_type = _REPLY
_REPLY.fields_by_name['actions'].message_type = _REPLY_ACTIONSENTRY
DESCRIPTOR.message_types_by_name['NormalScheduleRequest'] = _NORMALSCHEDULEREQUEST
DESCRIPTOR.message_types_by_name['SetpointExpansionRequest'] = _SETPOINTEXPANSIONREQUEST
DESCRIPTOR.message_types_by_name['DemandChargeRequest'] = _DEMANDCHARGEREQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NormalScheduleRequest = _reflection.GeneratedProtocolMessageType('NormalScheduleRequest', (_message.Message,), dict(

  StartingTemperaturesEntry = _reflection.GeneratedProtocolMessageType('StartingTemperaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _NORMALSCHEDULEREQUEST_STARTINGTEMPERATURESENTRY,
    __module__ = 'baseline_optimizer_pb2'
    # @@protoc_insertion_point(class_scope:baseline_optimizer.NormalScheduleRequest.StartingTemperaturesEntry)
    ))
  ,
  DESCRIPTOR = _NORMALSCHEDULEREQUEST,
  __module__ = 'baseline_optimizer_pb2'
  # @@protoc_insertion_point(class_scope:baseline_optimizer.NormalScheduleRequest)
  ))
_sym_db.RegisterMessage(NormalScheduleRequest)
_sym_db.RegisterMessage(NormalScheduleRequest.StartingTemperaturesEntry)

SetpointExpansionRequest = _reflection.GeneratedProtocolMessageType('SetpointExpansionRequest', (_message.Message,), dict(

  StartingTemperaturesEntry = _reflection.GeneratedProtocolMessageType('StartingTemperaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _SETPOINTEXPANSIONREQUEST_STARTINGTEMPERATURESENTRY,
    __module__ = 'baseline_optimizer_pb2'
    # @@protoc_insertion_point(class_scope:baseline_optimizer.SetpointExpansionRequest.StartingTemperaturesEntry)
    ))
  ,

  ExpansionDegreesEntry = _reflection.GeneratedProtocolMessageType('ExpansionDegreesEntry', (_message.Message,), dict(
    DESCRIPTOR = _SETPOINTEXPANSIONREQUEST_EXPANSIONDEGREESENTRY,
    __module__ = 'baseline_optimizer_pb2'
    # @@protoc_insertion_point(class_scope:baseline_optimizer.SetpointExpansionRequest.ExpansionDegreesEntry)
    ))
  ,
  DESCRIPTOR = _SETPOINTEXPANSIONREQUEST,
  __module__ = 'baseline_optimizer_pb2'
  # @@protoc_insertion_point(class_scope:baseline_optimizer.SetpointExpansionRequest)
  ))
_sym_db.RegisterMessage(SetpointExpansionRequest)
_sym_db.RegisterMessage(SetpointExpansionRequest.StartingTemperaturesEntry)
_sym_db.RegisterMessage(SetpointExpansionRequest.ExpansionDegreesEntry)

DemandChargeRequest = _reflection.GeneratedProtocolMessageType('DemandChargeRequest', (_message.Message,), dict(

  StartingTemperaturesEntry = _reflection.GeneratedProtocolMessageType('StartingTemperaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _DEMANDCHARGEREQUEST_STARTINGTEMPERATURESENTRY,
    __module__ = 'baseline_optimizer_pb2'
    # @@protoc_insertion_point(class_scope:baseline_optimizer.DemandChargeRequest.StartingTemperaturesEntry)
    ))
  ,
  DESCRIPTOR = _DEMANDCHARGEREQUEST,
  __module__ = 'baseline_optimizer_pb2'
  # @@protoc_insertion_point(class_scope:baseline_optimizer.DemandChargeRequest)
  ))
_sym_db.RegisterMessage(DemandChargeRequest)
_sym_db.RegisterMessage(DemandChargeRequest.StartingTemperaturesEntry)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), dict(

  ActionsEntry = _reflection.GeneratedProtocolMessageType('ActionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _REPLY_ACTIONSENTRY,
    __module__ = 'baseline_optimizer_pb2'
    # @@protoc_insertion_point(class_scope:baseline_optimizer.Reply.ActionsEntry)
    ))
  ,
  DESCRIPTOR = _REPLY,
  __module__ = 'baseline_optimizer_pb2'
  # @@protoc_insertion_point(class_scope:baseline_optimizer.Reply)
  ))
_sym_db.RegisterMessage(Reply)
_sym_db.RegisterMessage(Reply.ActionsEntry)


DESCRIPTOR._options = None
_NORMALSCHEDULEREQUEST_STARTINGTEMPERATURESENTRY._options = None
_SETPOINTEXPANSIONREQUEST_STARTINGTEMPERATURESENTRY._options = None
_SETPOINTEXPANSIONREQUEST_EXPANSIONDEGREESENTRY._options = None
_DEMANDCHARGEREQUEST_STARTINGTEMPERATURESENTRY._options = None
_REPLY_ACTIONSENTRY._options = None

_BASELINEOPTIMIZER = _descriptor.ServiceDescriptor(
  name='BaselineOptimizer',
  full_name='baseline_optimizer.BaselineOptimizer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1323,
  serialized_end=1958,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetNormalScheduleAction',
    full_name='baseline_optimizer.BaselineOptimizer.GetNormalScheduleAction',
    index=0,
    containing_service=None,
    input_type=_NORMALSCHEDULEREQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSetpointExpansionAction',
    full_name='baseline_optimizer.BaselineOptimizer.GetSetpointExpansionAction',
    index=1,
    containing_service=None,
    input_type=_SETPOINTEXPANSIONREQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDemandChargeAction',
    full_name='baseline_optimizer.BaselineOptimizer.GetDemandChargeAction',
    index=2,
    containing_service=None,
    input_type=_DEMANDCHARGEREQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNormalScheduleSimulation',
    full_name='baseline_optimizer.BaselineOptimizer.GetNormalScheduleSimulation',
    index=3,
    containing_service=None,
    input_type=_NORMALSCHEDULEREQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSetpointExpansionSimulation',
    full_name='baseline_optimizer.BaselineOptimizer.GetSetpointExpansionSimulation',
    index=4,
    containing_service=None,
    input_type=_SETPOINTEXPANSIONREQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDemandChargeSimualtion',
    full_name='baseline_optimizer.BaselineOptimizer.GetDemandChargeSimualtion',
    index=5,
    containing_service=None,
    input_type=_DEMANDCHARGEREQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BASELINEOPTIMIZER)

DESCRIPTOR.services_by_name['BaselineOptimizer'] = _BASELINEOPTIMIZER

# @@protoc_insertion_point(module_scope)