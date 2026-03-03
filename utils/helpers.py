from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_schema(response_json, schema):
    try:
        validate(instance=response_json, schema=schema)
    except ValidationError as e:
        raise AssertionError(f"Schema validation failed: {e.message}")