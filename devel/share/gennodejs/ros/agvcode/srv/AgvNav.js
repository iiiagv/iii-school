// Auto-generated. Do not edit!

// (in-package agvcode.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class AgvNavRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.coordinate = null;
    }
    else {
      if (initObj.hasOwnProperty('coordinate')) {
        this.coordinate = initObj.coordinate
      }
      else {
        this.coordinate = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type AgvNavRequest
    // Serialize message field [coordinate]
    bufferOffset = _serializer.string(obj.coordinate, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type AgvNavRequest
    let len;
    let data = new AgvNavRequest(null);
    // Deserialize message field [coordinate]
    data.coordinate = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.coordinate.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'agvcode/AgvNavRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c65ef28c342c0d5eee21ae18aad1bb8d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string coordinate
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new AgvNavRequest(null);
    if (msg.coordinate !== undefined) {
      resolved.coordinate = msg.coordinate;
    }
    else {
      resolved.coordinate = ''
    }

    return resolved;
    }
};

class AgvNavResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.status = null;
      this.error_msg = null;
    }
    else {
      if (initObj.hasOwnProperty('status')) {
        this.status = initObj.status
      }
      else {
        this.status = false;
      }
      if (initObj.hasOwnProperty('error_msg')) {
        this.error_msg = initObj.error_msg
      }
      else {
        this.error_msg = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type AgvNavResponse
    // Serialize message field [status]
    bufferOffset = _serializer.bool(obj.status, buffer, bufferOffset);
    // Serialize message field [error_msg]
    bufferOffset = _serializer.string(obj.error_msg, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type AgvNavResponse
    let len;
    let data = new AgvNavResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [error_msg]
    data.error_msg = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.error_msg.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'agvcode/AgvNavResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '426bb48ea6b00ad5853fdaddd836bcc6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool status
    string error_msg
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new AgvNavResponse(null);
    if (msg.status !== undefined) {
      resolved.status = msg.status;
    }
    else {
      resolved.status = false
    }

    if (msg.error_msg !== undefined) {
      resolved.error_msg = msg.error_msg;
    }
    else {
      resolved.error_msg = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: AgvNavRequest,
  Response: AgvNavResponse,
  md5sum() { return 'd314b4d308820390a64698753b2ba3b9'; },
  datatype() { return 'agvcode/AgvNav'; }
};
