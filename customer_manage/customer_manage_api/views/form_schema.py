TYPE_UINT64_MAX = 18446744073709551615

StringSchema = {"type": "string"}
UInt64Schema = {"type": "integer", "minimum": 0, "maximum": TYPE_UINT64_MAX}

CustomerSchema = {
    "type": "object",
    "properties": {
        "name": StringSchema,
        "dob": StringSchema
    },
    "required": ["name", "dob"]
}

CustomerInfoSchema = {
    "type": "object",
    "properties": {
        "ids": {
            "type": "array",
            "minItems": 0,
            "maxItems": 100,
            "delimiter": ",",
            "items": UInt64Schema
        },
    },
    "required": ["ids"]
}

CustomerUpdateSchema = {
    "type": "object",
    "properties": {
        "id": UInt64Schema,
        "name": StringSchema,
        "dob": StringSchema
    },
    "required": ["id"]
}

CustomerDeleteSchema = {
    "type": "object",
    "properties": {
        "id": UInt64Schema
    },
    "required": ["id"]
}