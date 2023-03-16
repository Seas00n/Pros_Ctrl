// Auto-generated. Do not edit!

// (in-package ros_ctrl.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Motor {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pos_desired = null;
      this.pos_actual = null;
      this.vel_desired = null;
      this.vel_actual = null;
      this.cur_desired = null;
      this.cur_actual = null;
      this.temperature = null;
      this.Kp = null;
      this.Kb = null;
      this.Angle_eq = null;
    }
    else {
      if (initObj.hasOwnProperty('pos_desired')) {
        this.pos_desired = initObj.pos_desired
      }
      else {
        this.pos_desired = 0.0;
      }
      if (initObj.hasOwnProperty('pos_actual')) {
        this.pos_actual = initObj.pos_actual
      }
      else {
        this.pos_actual = 0.0;
      }
      if (initObj.hasOwnProperty('vel_desired')) {
        this.vel_desired = initObj.vel_desired
      }
      else {
        this.vel_desired = 0.0;
      }
      if (initObj.hasOwnProperty('vel_actual')) {
        this.vel_actual = initObj.vel_actual
      }
      else {
        this.vel_actual = 0.0;
      }
      if (initObj.hasOwnProperty('cur_desired')) {
        this.cur_desired = initObj.cur_desired
      }
      else {
        this.cur_desired = 0.0;
      }
      if (initObj.hasOwnProperty('cur_actual')) {
        this.cur_actual = initObj.cur_actual
      }
      else {
        this.cur_actual = 0.0;
      }
      if (initObj.hasOwnProperty('temperature')) {
        this.temperature = initObj.temperature
      }
      else {
        this.temperature = 0.0;
      }
      if (initObj.hasOwnProperty('Kp')) {
        this.Kp = initObj.Kp
      }
      else {
        this.Kp = 0.0;
      }
      if (initObj.hasOwnProperty('Kb')) {
        this.Kb = initObj.Kb
      }
      else {
        this.Kb = 0.0;
      }
      if (initObj.hasOwnProperty('Angle_eq')) {
        this.Angle_eq = initObj.Angle_eq
      }
      else {
        this.Angle_eq = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Motor
    // Serialize message field [pos_desired]
    bufferOffset = _serializer.float64(obj.pos_desired, buffer, bufferOffset);
    // Serialize message field [pos_actual]
    bufferOffset = _serializer.float64(obj.pos_actual, buffer, bufferOffset);
    // Serialize message field [vel_desired]
    bufferOffset = _serializer.float64(obj.vel_desired, buffer, bufferOffset);
    // Serialize message field [vel_actual]
    bufferOffset = _serializer.float64(obj.vel_actual, buffer, bufferOffset);
    // Serialize message field [cur_desired]
    bufferOffset = _serializer.float64(obj.cur_desired, buffer, bufferOffset);
    // Serialize message field [cur_actual]
    bufferOffset = _serializer.float64(obj.cur_actual, buffer, bufferOffset);
    // Serialize message field [temperature]
    bufferOffset = _serializer.float64(obj.temperature, buffer, bufferOffset);
    // Serialize message field [Kp]
    bufferOffset = _serializer.float64(obj.Kp, buffer, bufferOffset);
    // Serialize message field [Kb]
    bufferOffset = _serializer.float64(obj.Kb, buffer, bufferOffset);
    // Serialize message field [Angle_eq]
    bufferOffset = _serializer.float64(obj.Angle_eq, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Motor
    let len;
    let data = new Motor(null);
    // Deserialize message field [pos_desired]
    data.pos_desired = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [pos_actual]
    data.pos_actual = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [vel_desired]
    data.vel_desired = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [vel_actual]
    data.vel_actual = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [cur_desired]
    data.cur_desired = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [cur_actual]
    data.cur_actual = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [temperature]
    data.temperature = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Kp]
    data.Kp = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Kb]
    data.Kb = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Angle_eq]
    data.Angle_eq = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 80;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_ctrl/Motor';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e4cbdf296cd255d692be25d05074c48d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 pos_desired
    float64 pos_actual
    float64 vel_desired
    float64 vel_actual
    float64 cur_desired
    float64 cur_actual
    float64 temperature
    float64 Kp
    float64 Kb
    float64 Angle_eq
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Motor(null);
    if (msg.pos_desired !== undefined) {
      resolved.pos_desired = msg.pos_desired;
    }
    else {
      resolved.pos_desired = 0.0
    }

    if (msg.pos_actual !== undefined) {
      resolved.pos_actual = msg.pos_actual;
    }
    else {
      resolved.pos_actual = 0.0
    }

    if (msg.vel_desired !== undefined) {
      resolved.vel_desired = msg.vel_desired;
    }
    else {
      resolved.vel_desired = 0.0
    }

    if (msg.vel_actual !== undefined) {
      resolved.vel_actual = msg.vel_actual;
    }
    else {
      resolved.vel_actual = 0.0
    }

    if (msg.cur_desired !== undefined) {
      resolved.cur_desired = msg.cur_desired;
    }
    else {
      resolved.cur_desired = 0.0
    }

    if (msg.cur_actual !== undefined) {
      resolved.cur_actual = msg.cur_actual;
    }
    else {
      resolved.cur_actual = 0.0
    }

    if (msg.temperature !== undefined) {
      resolved.temperature = msg.temperature;
    }
    else {
      resolved.temperature = 0.0
    }

    if (msg.Kp !== undefined) {
      resolved.Kp = msg.Kp;
    }
    else {
      resolved.Kp = 0.0
    }

    if (msg.Kb !== undefined) {
      resolved.Kb = msg.Kb;
    }
    else {
      resolved.Kb = 0.0
    }

    if (msg.Angle_eq !== undefined) {
      resolved.Angle_eq = msg.Angle_eq;
    }
    else {
      resolved.Angle_eq = 0.0
    }

    return resolved;
    }
};

module.exports = Motor;
