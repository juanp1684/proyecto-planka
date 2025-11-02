SCHEMA_CARD_PAYLOAD_INPUT = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "position": {
      "type": "number"
    },
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "dueDate": {
      "type": "string"
    },
    "isDueCompleted": {
      "type": "boolean"
    },
    "stopwatch": {
      "type": "object",
      "properties": {
        "startedAt": {
          "type": "string"
        },
        "total": {
          "type": "number"
        }
      },
      "required": [
        "startedAt",
        "total"
      ]
    }
  },
  "required": [
    "type",
    "position",
    "name",
    "description",
    "dueDate",
    "isDueCompleted",
    "stopwatch"
  ]
}


SCHEMA_CARD_WITH_STOPWATCH = {
    "type": "object",
    "properties": {
        "item": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "stopwatch": {
                    "type": "object",
                    "properties": {
                        "total": {"type": "number"},
                        "startedAt": {"type": "string"}
                    },
                    "required": ["total", "startedAt"]
                }
            },
            "required": ["id", "stopwatch"]
        }
    },
    "required": ["item"]
}


SCHEMA_CARD_WITHOUT_STOPWATCH = {
    "type": "object",
    "properties": {
        "item": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "stopwatch": {"type": ["null"]}
            },
            "required": ["id", "stopwatch"]
        }
    },
    "required": ["item"]
}
