schema_post_auth_successful = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "token": {
          "type": "string"
        }
      },
      "required": [
        "token"
      ]
    }
  },
  "required": [
    "status",
    "data"
  ]
}

schema_post_auth_unsuccessful = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "code": {
      "type": "integer"
    },
    "message": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "status": {
      "type": "integer"
    }
  },
  "required": [
    "code",
    "message",
    "name",
    "status"
  ]
}
