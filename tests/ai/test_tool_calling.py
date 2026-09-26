
from app.ai.tool_calling import (
    parse_tool_call,
    validate_tool_call,
    execute_tool_call
)
from app.tools.registry import register_tool


# 1. Parse a valid tool call

def test_parse_valid_tool_call():

    tool_call = {
        "name": "open_chrome",
        "arguments": {}
    }

    parsed, error = parse_tool_call(tool_call)

    assert error is None
    assert parsed == {
        "name": "open_chrome",
        "arguments": {}
    }


# 2. Parse JSON string arguments

def test_parse_json_string_arguments():

    tool_call = {
        "name": "file_exists",
        "arguments": '{"file_path": "test.txt"}'
    }

    parsed, error = parse_tool_call(tool_call)

    assert error is None

    assert parsed["arguments"] == {
        "file_path": "test.txt"
    }


# 3. Reject invalid JSON

def test_parse_invalid_json():

    tool_call = {
        "name": "file_exists",
        "arguments": '{"file_path": '
    }

    parsed, error = parse_tool_call(tool_call)

    assert parsed is None
    assert error == "Tool arguments contain invalid JSON."


# 4. Reject invalid tool call format

def test_parse_invalid_tool_call():

    parsed, error = parse_tool_call("invalid")

    assert parsed is None
    assert error == "Tool call must be a dictionary."


# 5. Reject missing required argument

def test_validate_missing_argument():

    error = validate_tool_call(
        "file_exists",
        {}
    )

    assert error == (
        "Missing required argument "
        "'file_path' for tool 'file_exists'."
    )


# 6. Reject incorrect argument type

def test_validate_wrong_argument_type():

    error = validate_tool_call(
        "file_exists",
        {
            "file_path": 123
        }
    )

    assert error == (
        "Argument 'file_path' must be a string."
    )


# 7. Reject unknown argument

def test_validate_unknown_argument():

    error = validate_tool_call(
        "open_chrome",
        {
            "unexpected": "value"
        }
    )

    assert error == (
        "Unknown argument 'unexpected' "
        "for tool 'open_chrome'."
    )


# 8. Reject unregistered tool

def test_validate_unknown_tool():

    error = validate_tool_call(
        "unknown_tool",
        {}
    )

    assert error == (
        "Tool 'unknown_tool' is not registered."
    )


# 9. Execute a valid tool call

def test_execute_valid_tool_call():

    register_tool(
        "mock_greeting",
        lambda: "Hello from mock",
        {
            "description": "Returns a mock greeting.",
            "parameters": {}
        }
    )

    result = execute_tool_call({
        "name": "mock_greeting",
        "arguments": {}
    })

    assert result == "Hello from mock"


def test_execute_openai_style_tool_call():

    register_tool(
        "mock_add",
        lambda a, b: a + b,
        {
            "description": "Adds two numbers.",
            "parameters": {
                "a": "int",
                "b": "int"
            }
        }
    )

    result = execute_tool_call({
        "function": {
            "name": "mock_add",
            "arguments": '{"a": 10, "b": 20}'
        }
    })

    assert result == 30


def test_search_file_directory_is_optional():

    error = validate_tool_call(
        "search_file",
        {
            "file_name": "main.py"
        }
    )

    assert error is None


def test_search_file_missing_required_argument():

    error = validate_tool_call(
        "search_file",
        {}
    )

    assert error == (
        "Missing required argument "
        "'file_name' for tool 'search_file'."
    )


def test_search_file_rejects_unknown_argument():

    error = validate_tool_call(
        "search_file",
        {
            "file_name": "main.py",
            "unknown": "value"
        }
    )

    assert error == (
        "Unknown argument 'unknown' for tool 'search_file'."
    )


def test_search_file_rejects_invalid_argument_type():

    error = validate_tool_call(
        "search_file",
        {
            "file_name": 123
        }
    )

    assert error == "Argument 'file_name' must be a string."


def test_search_file_schema_marks_directory_optional():

    from app.tools.registry import get_tool_schema

    schema = get_tool_schema("search_file")

    parameters = schema["function"]["parameters"]

    assert "file_name" in parameters["required"]

    assert "search_directory" not in parameters["required"]


def test_search_file_executes_without_directory():

    result = execute_tool_call({
        "name": "search_file",
        "arguments": {
            "file_name": "this_file_should_not_exist_zyro.txt"
        }
    })

    assert result == (
        "I could not find this_file_should_not_exist_zyro.txt."
    )