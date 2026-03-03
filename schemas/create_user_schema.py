create_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "job": {"type": "string"}
    },
    "required": ["name", "job", "id"]
}