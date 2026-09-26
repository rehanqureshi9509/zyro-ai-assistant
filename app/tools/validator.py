from app.tools.registry import (
    get_all_tools,
    get_all_tool_metadata
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