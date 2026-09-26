
from app.tools.registry import (
    register_tool,
    get_tool,
    get_all_tools,
    execute_tool,
    get_tool_metadata,
    get_all_tool_metadata
)

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


# 1. Register a tool with metadata

def test_register_tool():

    def test_function():
        return "Test successful"

    metadata = {
        "description": "Test tool.",
        "parameters": {}
    }

    register_tool(
        "test_tool",
        test_function,
        metadata
    )

    assert get_tool("test_tool") == test_function
    assert get_tool_metadata("test_tool") == metadata


# 2. Get missing tool

def test_get_missing_tool():

    result = get_tool("missing_tool")

    assert result is None


# 3. Get all tools

def test_get_all_tools():

    def another_function():
        return "Another test"

    metadata = {
        "description": "Another test tool.",
        "parameters": {}
    }

    register_tool(
        "another_tool",
        another_function,
        metadata
    )

    tools = get_all_tools()

    assert "another_tool" in tools
    assert tools["another_tool"] == another_function


# 4. Execute tool

def test_execute_tool():

    def greeting():
        return "Hello from tool"

    register_tool(
        "greeting",
        greeting,
        {
            "description": "Returns a greeting.",
            "parameters": {}
        }
    )

    result = execute_tool("greeting")

    assert result == "Hello from tool"


# 5. Execute tool with arguments

def test_execute_tool_with_arguments():

    def add_numbers(a, b):
        return a + b

    register_tool(
        "add_numbers",
        add_numbers,
        {
            "description": "Adds two numbers.",
            "parameters": {
                "a": "int",
                "b": "int"
            }
        }
    )

    result = execute_tool(
        "add_numbers",
        10,
        20
    )

    assert result == 30


# 6. Execute missing tool

def test_execute_missing_tool():

    result = execute_tool("missing_tool")

    assert result == (
        "Tool 'missing_tool' is not registered."
    )


# 7. Verify all Zyro tools are registered

def test_existing_zyro_tools_are_registered():

    tools = get_all_tools()

    assert "open_notepad" in tools
    assert "open_calculator" in tools
    assert "open_chrome" in tools
    assert "open_vscode" in tools

    assert "lock_computer" in tools
    assert "restart_computer" in tools
    assert "shutdown_computer" in tools

    assert "search_file" in tools

    assert "file_exists" in tools
    assert "directory_exists" in tools
    assert "get_file_info" in tools
    assert "create_directory" in tools
    assert "list_files" in tools


# 8. Get tool metadata

def test_get_tool_metadata():

    metadata = get_tool_metadata("open_chrome")

    assert metadata["description"] == "Opens Google Chrome."
    assert metadata["parameters"] == {}


# 9. Get file tool metadata

def test_get_file_tool_metadata():

    metadata = get_tool_metadata("search_file")

    assert metadata["description"] == (
        "Searches for a file in a directory."
    )

    assert metadata["parameters"] == {
        "file_name": "str",
        "search_directory": "str"
    }


# 10. Get missing tool metadata

def test_get_missing_tool_metadata():

    result = get_tool_metadata("missing_tool")

    assert result is None


# 11. Get all tool metadata

def test_get_all_tool_metadata():

    metadata = get_all_tool_metadata()

    assert "open_chrome" in metadata
    assert "search_file" in metadata
    assert "create_directory" in metadata


# 12. All registered tools have metadata

def test_all_registered_tools_have_metadata():

    tools = get_all_tools()
    metadata = get_all_tool_metadata()

    for tool_name in tools:

        assert tool_name in metadata


# 13. All registered metadata is valid

def test_all_registered_metadata_is_valid():

    from app.tools.validator import validate_all_tools

    errors = validate_all_tools()

    assert errors == []