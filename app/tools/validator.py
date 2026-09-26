from app.tools.registry import (
    get_all_tools,
    get_all_tool_metadata,
    get_tool_metadata,
    get_tool_schema
)


def validate_tool_metadata(name, metadata):

    if not isinstance(name, str) or not name.strip():

        return False

    if not isinstance(metadata, dict):

        return False

    description = metadata.get("description")

    if not isinstance(description, str) or not description.strip():

        return False

    parameters = metadata.get("parameters")

    if not isinstance(parameters, dict):

        return False

    for parameter_name, parameter_type in parameters.items():

        if not isinstance(parameter_name, str):
            return False

        if not parameter_name.strip():
            return False

        if not isinstance(parameter_type, str):
            return False

        if not parameter_type.strip():
            return False

    return True


def validate_all_tools():

    tools = get_all_tools()

    metadata = get_all_tool_metadata()

    errors = []

    for tool_name in tools:

        tool_metadata = metadata.get(tool_name)

        if tool_metadata is None:

            errors.append(
                f"Missing metadata for tool: {tool_name}"
            )

            continue

        if not validate_tool_metadata(
            tool_name,
            tool_metadata
        ):

            errors.append(
                f"Invalid metadata for tool: {tool_name}"
            )

    return errors

def validate_tool_schema(name):

    errors = []

    schema = get_tool_schema(name)

    if not isinstance(schema, dict):
        return [f"Invalid or missing schema for tool '{name}'."]

    if schema.get("type") != "function":
        errors.append(
            f"Tool '{name}' schema type must be 'function'."
        )

    function_schema = schema.get("function")

    if not isinstance(function_schema, dict):
        return [f"Invalid function schema for tool '{name}'."]

    if function_schema.get("name") != name:
        errors.append(
            f"Schema name mismatch for tool '{name}'."
        )

    parameters = function_schema.get("parameters")

    if not isinstance(parameters, dict):
        errors.append(
            f"Invalid parameters schema for tool '{name}'."
        )
        return errors

    if parameters.get("type") != "object":
        errors.append(
            f"Parameters type must be 'object' for tool '{name}'."
        )

    properties = parameters.get("properties")

    if not isinstance(properties, dict):
        errors.append(
            f"Properties must be a dictionary for tool '{name}'."
        )
        return errors

    required = parameters.get("required", [])

    if not isinstance(required, list):
        errors.append(
            f"Required parameters must be a list for tool '{name}'."
        )
        return errors

    for parameter_name in required:

        if parameter_name not in properties:
            errors.append(
                f"Required parameter '{parameter_name}' "
                f"is not defined in tool '{name}'."
            )

    for parameter_name, property_schema in properties.items():

        if not isinstance(property_schema, dict):
            errors.append(
                f"Invalid schema for parameter '{parameter_name}' "
                f"in tool '{name}'."
            )
            continue

        if property_schema.get("type") not in {
            "string",
            "integer",
            "number",
            "boolean"
        }:
            errors.append(
                f"Unsupported schema type for parameter "
                f"'{parameter_name}' in tool '{name}'."
            )

    return errors

def validate_tool_registry():

    errors = []

    tool_names = get_all_tools()
    metadata = get_all_tool_metadata()

    if not isinstance(metadata, dict):
        return ["Tool metadata registry must be a dictionary."]

    for tool_name in tool_names:

        tool_metadata = get_tool_metadata(tool_name)

        if tool_metadata is None:
            errors.append(
                f"Metadata missing for tool '{tool_name}'."
            )
            continue

        # Existing validator returns True or False
        metadata_is_valid = validate_tool_metadata(
            tool_name,
            tool_metadata
        )

        if metadata_is_valid is False:
            errors.append(
                f"Invalid metadata for tool '{tool_name}'."
            )

        # Schema validator returns a list of errors
        schema_errors = validate_tool_schema(tool_name)

        errors.extend(schema_errors)

    return errors