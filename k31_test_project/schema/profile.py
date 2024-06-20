schema_user_profile = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "email": {
          "type": "string"
        },
        "username": {
          "type": "string"
        },
        "last_name": {
          "type": "string"
        },
        "first_name": {
          "type": "string"
        },
        "middle_name": {
          "type": "string"
        },
        "card": {
          "type": "string"
        },
        "photo": {
          "type": "null"
        },
        "gender_id": {
          "type": "integer"
        },
        "gender": {
          "type": "string"
        },
        "birthday": {
          "type": "string"
        },
        "icon": {
          "type": "string"
        },
        "ex_element_id": {
          "type": "null"
        },
        "is_telemed": {
          "type": "integer"
        },
        "is_admin": {
          "type": "boolean"
        },
        "is_patient": {
          "type": "boolean"
        },
        "dms_id": {
          "type": "null"
        },
        "dms_name": {
          "type": "null"
        },
        "oms_id": {
          "type": "null"
        },
        "oms_name": {
          "type": "null"
        },
        "blood_type": {
          "type": "null"
        },
        "rhesus_factor": {
          "type": "null"
        },
        "family_cards": {
          "type": "array",
          "items": {}
        },
        "family_cards_disabled": {
          "type": "array",
          "items": {}
        },
        "is_email_verified": {
          "type": "boolean"
        },
        "is_agreement": {
          "type": "integer"
        },
        "is_form_patient": {
          "type": "integer"
        },
        "is_vip": {
          "type": "boolean"
        },
        "vip_status": {
          "type": "null"
        },
        "is_pin": {
          "type": "boolean"
        }
      },
      "required": [
        "id",
        "email",
        "username",
        "last_name",
        "first_name",
        "middle_name",
        "card",
        "photo",
        "gender_id",
        "gender",
        "birthday",
        "icon",
        "ex_element_id",
        "is_telemed",
        "is_admin",
        "is_patient",
        "dms_id",
        "dms_name",
        "oms_id",
        "oms_name",
        "blood_type",
        "rhesus_factor",
        "family_cards",
        "family_cards_disabled",
        "is_email_verified",
        "is_agreement",
        "is_form_patient",
        "is_vip",
        "vip_status",
        "is_pin"
      ]
    }
  },
  "required": [
    "status",
    "data"
  ]
}

schema_have_no_car = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "data": {
      "type": "array",
      "items": {}
    }
  },
  "required": [
    "status",
    "data"
  ]
}

schema_post_add_car = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "model": {
          "type": "string"
        },
        "number": {
          "type": "string"
        },
        "is_primary": {
          "type": "integer"
        }
      },
      "required": [
        "id",
        "model",
        "number",
        "is_primary"
      ]
    }
  },
  "required": [
    "status",
    "data"
  ]
}

schema_delete_car = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "status",
    "message"
  ]
}

schema_car_access_denied = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "error_code": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "status",
    "error_code",
    "message"
  ]
}

schema_car_list = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "data": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "model": {
              "type": "string"
            },
            "number": {
              "type": "string"
            },
            "is_primary": {
              "type": "integer"
            }
          },
          "required": [
            "id",
            "model",
            "number",
            "is_primary"
          ]
        }
      ]
    }
  },
  "required": [
    "status",
    "data"
  ]
}