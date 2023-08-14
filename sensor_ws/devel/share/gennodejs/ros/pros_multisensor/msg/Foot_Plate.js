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
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Foot_Plate
    // Serialize message field [F_area1]
    bufferOffset = _serializer.float64(obj.F_area1, buffer, bufferOffset);
    // Serialize message field [x_area1]
    bufferOffset = _serializer.float64(obj.x_area1, buffer, bufferOffset);
    // Serialize message field [y_area1]
    bufferOffset = _serializer.float64(obj.y_area1, buffer, bufferOffset);
    // Serialize message field [F_area2]
    bufferOffset = _serializer.float64(obj.F_area2, buffer, bufferOffset);
    // Serialize message field [x_area2]
    bufferOffset = _serializer.float64(obj.x_area2, buffer, bufferOffset);
    // Serialize message field [y_area2]
    bufferOffset = _serializer.float64(obj.y_area2, buffer, bufferOffset);
    // Serialize message field [F_area3]
    bufferOffset = _serializer.float64(obj.F_area3, buffer, bufferOffset);
    // Serialize message field [x_area3]
    bufferOffset = _serializer.float64(obj.x_area3, buffer, bufferOffset);
    // Serialize message field [y_area3]
    bufferOffset = _serializer.float64(obj.y_area3, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Foot_Plate
    let len;
    let data = new Foot_Plate(null);
    // Deserialize message field [F_area1]
    data.F_area1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [x_area1]
    data.x_area1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_area1]
    data.y_area1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [F_area2]
    data.F_area2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [x_area2]
    data.x_area2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_area2]
    data.y_area2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [F_area3]
    data.F_area3 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [x_area3]
    data.x_area3 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_area3]
    data.y_area3 = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 72;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pros_multisensor/Foot_Plate';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8abe2ed9ca3a52015264ef11ea8b519b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 F_area1
    float64 x_area1
    float64 y_area1
    float64 F_area2
    float64 x_area2
    float64 y_area2
    float64 F_area3
    float64 x_area3
    float64 y_area3
    
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

    return resolved;
    }
};

module.exports = Foot_Plate;
