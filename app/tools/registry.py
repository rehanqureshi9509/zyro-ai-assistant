
from app.tools.windows.applications import (
    open_notepad,
    open_calculator,
    open_chrome,
    open_vscode
)

from app.tools.windows.system import (
    lock_computer,
    restart_computer,
    shutdown_computer
)

from app.tools.files.search import search_file

from app.tools.files.manager import (
    file_exists,
    directory_exists,
    get_file_info,
    create_directory,
    list_files
)


TOOLS = {}

TOOL_METADATA = {}


def register_tool(name, function, metadata=None):

    TOOLS[name] = function

    if metadata is not None:
        TOOL_METADATA[name] = metadata


def get_tool(name):

    return TOOLS.get(name)


def get_all_tools():

    return TOOLS.copy()



def execute_tool(name, *args, **kwargs):

    from app.tools.executor import execute_tool as run_tool

    return run_tool(name, *args, **kwargs)


def get_tool_metadata(name):

    return TOOL_METADATA.get(name)


def get_all_tool_metadata():

    return TOOL_METADATA.copy()


def get_tool_schema(name):

    metadata = get_tool_metadata(name)

    if metadata is None:
        return None

    parameters = metadata.get("parameters", {})

    properties = {}

    for parameter_name, parameter_type in parameters.items():

        if parameter_type == "str":
            json_type = "string"

        elif parameter_type == "int":
            json_type = "integer"

        elif parameter_type == "float":
            json_type = "number"

        elif parameter_type == "bool":
            json_type = "boolean"

        else:
            json_type = "string"

        properties[parameter_name] = {
            "type": json_type,
            "description": f"Value for {parameter_name}"
        }

    return {
        "type": "function",
        "function": {
            "name": name,
            "description": metadata["description"],
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": list(parameters.keys())
            }
        }
    }


def get_all_tool_schemas():

    tools = get_all_tools()

    schemas = []

    for tool_name in tools:

        schema = get_tool_schema(tool_name)

        if schema is not None:
            schemas.append(schema)

    return schemas


# Register Windows application tools

register_tool(
    "open_notepad",
    open_notepad,
    {
        "description": "Opens Notepad.",
        "parameters": {}
    }
)

register_tool(
    "open_calculator",
    open_calculator,
    {
        "description": "Opens Windows Calculator.",
        "parameters": {}
    }
)

register_tool(
    "open_chrome",
    open_chrome,
    {
        "description": "Opens Google Chrome.",
        "parameters": {}
    }
)

register_tool(
    "open_vscode",
    open_vscode,
    {
        "description": "Opens Visual Studio Code.",
        "parameters": {}
    }
)


# Register Windows system tools

register_tool(
    "lock_computer",
    lock_computer,
    {
        "description": "Locks the Windows computer.",
        "parameters": {}
    }
)

register_tool(
    "restart_computer",
    restart_computer,
    {
        "description": "Prepares a computer restart.",
        "parameters": {}
    }
)

register_tool(
    "shutdown_computer",
    shutdown_computer,
    {
        "description": "Prepares a computer shutdown.",
        "parameters": {}
    }
)


# Register file search tool

register_tool(
    "search_file",
    search_file,
    {
        "description": "Searches for a file in a directory.",
        "parameters": {
            "file_name": "str",
            "search_directory": "str"
        }
    }
)


# Register file management tools

register_tool(
    "file_exists",
    file_exists,
    {
        "description": "Checks whether a file exists.",
        "parameters": {
            "file_path": "str"
        }
    }
)

register_tool(
    "directory_exists",
    directory_exists,
    {
        "description": "Checks whether a directory exists.",
        "parameters": {
            "directory_path": "str"
        }
    }
)

register_tool(
    "get_file_info",
    get_file_info,
    {
        "description": "Gets information about a file.",
        "parameters": {
            "file_path": "str"
        }
    }
)

register_tool(
    "create_directory",
    create_directory,
    {
        "description": "Creates a directory.",
        "parameters": {
            "directory_path": "str"
        }
    }
)

register_tool(
    "list_files",
    list_files,
    {
        "description": "Lists files inside a directory.",
        "parameters": {
            "directory_path": "str"
        }
    }
)