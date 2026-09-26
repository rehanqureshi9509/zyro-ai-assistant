
import json

from app.tools.registry import (
    get_tool,
    get_tool_metadata
)

from app.tools.executor import execute_tool


def parse_tool_call(tool_call):

    if not isinstance(tool_call, dict):
        return None, "Tool call must be a dictionary."

    # Support both direct and OpenAI-style function calls
    function_data = tool_call.get("function", tool_call)

    if not isinstance(function_data, dict):
        return None, "Invalid function data."

    tool_name = function_data.get("name")
    arguments = function_data.get("arguments", {})

    if not isinstance(tool_name, str) or not tool_name.strip():
        return None, "Tool name is missing or invalid."

    # AI may return arguments as a JSON string
    if isinstance(arguments, str):

        try:
            arguments = json.loads(arguments)

        except json.JSONDecodeError:
            return None, "Tool arguments contain invalid JSON."

    if not isinstance(arguments, dict):
        return None, "Tool arguments must be a JSON object."

    return {
        "name": tool_name,
        "arguments": arguments
    }, None

def validate_tool_call(tool_name, arguments):

    tool = get_tool(tool_name)

    if tool is None:
        return f"Tool '{tool_name}' is not registered."

    metadata = get_tool_metadata(tool_name)

    if not isinstance(metadata, dict):
        return f"Metadata for tool '{tool_name}' is missing."

    parameters = metadata.get("parameters")
    optional_parameters = metadata.get("optional_parameters", [])

    if not isinstance(parameters, dict):
        return f"Invalid parameter metadata for '{tool_name}'."

    if not isinstance(optional_parameters, list):
        return f"Invalid optional parameter metadata for '{tool_name}'."

    # Check optional parameter definitions
    for parameter_name in optional_parameters:

        if parameter_name not in parameters:
            return (
                f"Optional parameter '{parameter_name}' "
                f"is not defined for tool '{tool_name}'."
            )

    # Reject unknown arguments
    for argument_name in arguments:

        if argument_name not in parameters:
            return (
                f"Unknown argument '{argument_name}' "
                f"for tool '{tool_name}'."
            )

    # Check required arguments
    for parameter_name, parameter_type in parameters.items():

        if parameter_name not in arguments:

            if parameter_name in optional_parameters:
                continue

            return (
                f"Missing required argument "
                f"'{parameter_name}' for tool '{tool_name}'."
            )

        value = arguments[parameter_name]

        if parameter_type == "str":

            if not isinstance(value, str):
                return (
                    f"Argument '{parameter_name}' "
                    f"must be a string."
                )

        elif parameter_type == "int":

            if isinstance(value, bool) or not isinstance(value, int):
                return (
                    f"Argument '{parameter_name}' "
                    f"must be an integer."
                )

        elif parameter_type == "float":

            if isinstance(value, bool) or not isinstance(value, (int, float)):
                return (
                    f"Argument '{parameter_name}' "
                    f"must be a number."
                )

        elif parameter_type == "bool":

            if not isinstance(value, bool):
                return (
                    f"Argument '{parameter_name}' "
                    f"must be a boolean."
                )

        else:
            return (
                f"Unsupported parameter type "
                f"'{parameter_type}' for '{parameter_name}'."
            )

    return None

def execute_tool_call(tool_call):

    parsed_call, error = parse_tool_call(tool_call)

    if error:
        return error

    tool_name = parsed_call["name"]
    arguments = parsed_call["arguments"]

    validation_error = validate_tool_call(
        tool_name,
        arguments
    )

    if validation_error:
        return validation_error

    return execute_tool(
        tool_name,
        **arguments
    )