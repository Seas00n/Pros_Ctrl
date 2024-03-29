# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from pros_multisensor/Foot_Plate.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Foot_Plate(genpy.Message):
  _md5sum = "e96a18f41c104b55b04d72c552abf512"
  _type = "pros_multisensor/Foot_Plate"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 F_area1
float32 x_area1
float32 y_area1
float32 F_area2
float32 x_area2
float32 y_area2
float32 F_area3
float32 x_area3
float32 y_area3
float32 F_net
float32 x_net
float32 y_net
int8 contact
"""
  __slots__ = ['F_area1','x_area1','y_area1','F_area2','x_area2','y_area2','F_area3','x_area3','y_area3','F_net','x_net','y_net','contact']
  _slot_types = ['float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       F_area1,x_area1,y_area1,F_area2,x_area2,y_area2,F_area3,x_area3,y_area3,F_net,x_net,y_net,contact

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Foot_Plate, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.F_area1 is None:
        self.F_area1 = 0.
      if self.x_area1 is None:
        self.x_area1 = 0.
      if self.y_area1 is None:
        self.y_area1 = 0.
      if self.F_area2 is None:
        self.F_area2 = 0.
      if self.x_area2 is None:
        self.x_area2 = 0.
      if self.y_area2 is None:
        self.y_area2 = 0.
      if self.F_area3 is None:
        self.F_area3 = 0.
      if self.x_area3 is None:
        self.x_area3 = 0.
      if self.y_area3 is None:
        self.y_area3 = 0.
      if self.F_net is None:
        self.F_net = 0.
      if self.x_net is None:
        self.x_net = 0.
      if self.y_net is None:
        self.y_net = 0.
      if self.contact is None:
        self.contact = 0
    else:
      self.F_area1 = 0.
      self.x_area1 = 0.
      self.y_area1 = 0.
      self.F_area2 = 0.
      self.x_area2 = 0.
      self.y_area2 = 0.
      self.F_area3 = 0.
      self.x_area3 = 0.
      self.y_area3 = 0.
      self.F_net = 0.
      self.x_net = 0.
      self.y_net = 0.
      self.contact = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_12fb().pack(_x.F_area1, _x.x_area1, _x.y_area1, _x.F_area2, _x.x_area2, _x.y_area2, _x.F_area3, _x.x_area3, _x.y_area3, _x.F_net, _x.x_net, _x.y_net, _x.contact))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 49
      (_x.F_area1, _x.x_area1, _x.y_area1, _x.F_area2, _x.x_area2, _x.y_area2, _x.F_area3, _x.x_area3, _x.y_area3, _x.F_net, _x.x_net, _x.y_net, _x.contact,) = _get_struct_12fb().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_12fb().pack(_x.F_area1, _x.x_area1, _x.y_area1, _x.F_area2, _x.x_area2, _x.y_area2, _x.F_area3, _x.x_area3, _x.y_area3, _x.F_net, _x.x_net, _x.y_net, _x.contact))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 49
      (_x.F_area1, _x.x_area1, _x.y_area1, _x.F_area2, _x.x_area2, _x.y_area2, _x.F_area3, _x.x_area3, _x.y_area3, _x.F_net, _x.x_net, _x.y_net, _x.contact,) = _get_struct_12fb().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_12fb = None
def _get_struct_12fb():
    global _struct_12fb
    if _struct_12fb is None:
        _struct_12fb = struct.Struct("<12fb")
    return _struct_12fb
