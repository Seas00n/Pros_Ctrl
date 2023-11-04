// Auto-generated. Do not edit!

// (in-package pros_multisensor.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Foot_Plate {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.F_area1 = null;
      this.x_area1 = null;
      this.y_area1 = null;
      this.F_area2 = null;
      this.x_area2 = null;
      this.y_area2 = null;
      this.F_area3 = null;
      this.x_area3 = null;
      this.y_area3 = null;
      this.F_net = null;
      this.x_net = null;
      this.y_net = null;
      this.contact = null;
    }
    else {
      if (initObj.hasOwnProperty('F_area1')) {
        this.F_area1 = initObj.F_area1
      }
      else {
        this.F_area1 = 0.0;
      }
      if (initObj.hasOwnProperty('x_area1')) {
        this.x_area1 = initObj.x_area1
      }
      else {
        this.x_area1 = 0.0;
      }
      if (initObj.hasOwnProperty('y_area1')) {
        this.y_area1 = initObj.y_area1
      }
      else {
        this.y_area1 = 0.0;
      }
      if (initObj.hasOwnProperty('F_area2')) {
        this.F_area2 = initObj.F_area2
      }
      else {
        this.F_area2 = 0.0;
      }
      if (initObj.hasOwnProperty('x_area2')) {
        this.x_area2 = initObj.x_area2
      }
      else {
        this.x_area2 = 0.0;
      }
      if (initObj.hasOwnProperty('y_area2')) {
        this.y_area2 = initObj.y_area2
      }
      else {
        this.y_area2 = 0.0;
      }
      if (initObj.hasOwnProperty('F_area3')) {
        this.F_area3 = initObj.F_area3
      }
      else {
        this.F_area3 = 0.0;
      }
      if (initObj.hasOwnProperty('x_area3')) {
        this.x_area3 = initObj.x_area3
      }
      else {
        this.x_area3 = 0.0;
      }
      if (initObj.hasOwnProperty('y_area3')) {
        this.y_area3 = initObj.y_area3
      }
      else {
        this.y_area3 = 0.0;
      }
      if (initObj.hasOwnProperty('F_net')) {
        this.F_net = initObj.F_net
      }
      else {
        this.F_net = 0.0;
      }
      if (initObj.hasOwnProperty('x_net')) {
        this.x_net = initObj.x_net
      }
      else {
        this.x_net = 0.0;
      }
      if (initObj.hasOwnProperty('y_net')) {
        this.y_net = initObj.y_net
      }
      else {
        this.y_net = 0.0;
      }
      if (initObj.hasOwnProperty('contact')) {
        this.contact = initObj.contact
      }
      else {
        this.contact = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Foot_Plate
    // Serialize message field [F_area1]
    bufferOffset = _serializer.float32(obj.F_area1, buffer, bufferOffset);
    // Serialize message field [x_area1]
    bufferOffset = _serializer.float32(obj.x_area1, buffer, bufferOffset);
    // Serialize message field [y_area1]
    bufferOffset = _serializer.float32(obj.y_area1, buffer, bufferOffset);
    // Serialize message field [F_area2]
    bufferOffset = _serializer.float32(obj.F_area2, buffer, bufferOffset);
    // Serialize message field [x_area2]
    bufferOffset = _serializer.float32(obj.x_area2, buffer, bufferOffset);
    // Serialize message field [y_area2]
    bufferOffset = _serializer.float32(obj.y_area2, buffer, bufferOffset);
    // Serialize message field [F_area3]
    bufferOffset = _serializer.float32(obj.F_area3, buffer, bufferOffset);
    // Serialize message field [x_area3]
    bufferOffset = _serializer.float32(obj.x_area3, buffer, bufferOffset);
    // Serialize message field [y_area3]
    bufferOffset = _serializer.float32(obj.y_area3, buffer, bufferOffset);
    // Serialize message field [F_net]
    bufferOffset = _serializer.float32(obj.F_net, buffer, bufferOffset);
    // Serialize message field [x_net]
    bufferOffset = _serializer.float32(obj.x_net, buffer, bufferOffset);
    // Serialize message field [y_net]
    bufferOffset = _serializer.float32(obj.y_net, buffer, bufferOffset);
    // Serialize message field [contact]
    bufferOffset = _serializer.int8(obj.contact, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Foot_Plate
    let len;
    let data = new Foot_Plate(null);
    // Deserialize message field [F_area1]
    data.F_area1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [x_area1]
    data.x_area1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y_area1]
    data.y_area1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [F_area2]
    data.F_area2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [x_area2]
    data.x_area2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y_area2]
    data.y_area2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [F_area3]
    data.F_area3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [x_area3]
    data.x_area3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y_area3]
    data.y_area3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [F_net]
    data.F_net = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [x_net]
    data.x_net = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y_net]
    data.y_net = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [contact]
    data.contact = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 49;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pros_multisensor/Foot_Plate';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e96a18f41c104b55b04d72c552abf512';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 F_area1
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Foot_Plate(null);
    if (msg.F_area1 !== undefined) {
      resolved.F_area1 = msg.F_area1;
    }
    else {
      resolved.F_area1 = 0.0
    }

    if (msg.x_area1 !== undefined) {
      resolved.x_area1 = msg.x_area1;
    }
    else {
      resolved.x_area1 = 0.0
    }

    if (msg.y_area1 !== undefined) {
      resolved.y_area1 = msg.y_area1;
    }
    else {
      resolved.y_area1 = 0.0
    }

    if (msg.F_area2 !== undefined) {
      resolved.F_area2 = msg.F_area2;
    }
    else {
      resolved.F_area2 = 0.0
    }

    if (msg.x_area2 !== undefined) {
      resolved.x_area2 = msg.x_area2;
    }
    else {
      resolved.x_area2 = 0.0
    }

    if (msg.y_area2 !== undefined) {
      resolved.y_area2 = msg.y_area2;
    }
    else {
      resolved.y_area2 = 0.0
    }

    if (msg.F_area3 !== undefined) {
      resolved.F_area3 = msg.F_area3;
    }
    else {
      resolved.F_area3 = 0.0
    }

    if (msg.x_area3 !== undefined) {
      resolved.x_area3 = msg.x_area3;
    }
    else {
      resolved.x_area3 = 0.0
    }

    if (msg.y_area3 !== undefined) {
      resolved.y_area3 = msg.y_area3;
    }
    else {
      resolved.y_area3 = 0.0
    }

    if (msg.F_net !== undefined) {
      resolved.F_net = msg.F_net;
    }
    else {
      resolved.F_net = 0.0
    }

    if (msg.x_net !== undefined) {
      resolved.x_net = msg.x_net;
    }
    else {
      resolved.x_net = 0.0
    }

    if (msg.y_net !== undefined) {
      resolved.y_net = msg.y_net;
    }
    else {
      resolved.y_net = 0.0
    }

    if (msg.contact !== undefined) {
      resolved.contact = msg.contact;
    }
    else {
      resolved.contact = 0
    }

    return resolved;
    }
};

module.exports = Foot_Plate;
