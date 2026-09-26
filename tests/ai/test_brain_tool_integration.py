from app.core.brain import process_ai_tool_call
from app.tools.registry import register_tool


def test_brain_executes_ai_tool_call():

    register_tool(
        "brain_test_greeting",
        lambda: "Hello from Zyro",
        {
            "description": "Returns a greeting.",
            "parameters": {}
        }
    )

    result = process_ai_tool_call({
        "name": "brain_test_greeting",
        "arguments": {}
    })

    assert result == "Hello from Zyro"


def test_brain_handles_unknown_tool():

    result = process_ai_tool_call({
        "name": "unknown_brain_tool",
        "arguments": {}
    })

    assert result == (
        "Tool 'unknown_brain_tool' is not registered."
    )


def test_brain_handles_invalid_arguments():

    result = process_ai_tool_call({
        "name": "file_exists",
        "arguments": {}
    })

    assert result == (
        "Missing required argument "
        "'file_path' for tool 'file_exists'."
    )


def test_brain_blocks_shutdown_without_confirmation():

    result = process_ai_tool_call({
        "name": "shutdown_computer",
        "arguments": {}
    })

    assert result == (
        "Confirmation required to execute 'shutdown_computer'."
    )


def test_brain_blocks_invalid_confirmation_value():

    result = process_ai_tool_call({
        "name": "shutdown_computer",
        "arguments": {},
        "confirmed": "yes"
    })

    assert result == "Confirmation value must be a boolean."

def test_end_to_end_normal_tool_call():

    result = process_ai_tool_call({
        "name": "file_exists",
        "arguments": {
            "file_path": "zyro_test_file_not_found.txt"
        }
    })

    assert result is False


def test_end_to_end_blocks_system_tool_without_confirmation():

    result = process_ai_tool_call({
        "name": "shutdown_computer",
        "arguments": {}
    })

    assert result == (
        "Confirmation required to execute 'shutdown_computer'."
    )


def test_end_to_end_allows_confirmed_system_tool():

    result = process_ai_tool_call({
        "name": "shutdown_computer",
        "arguments": {},
        "confirmed": True
    })

    assert result == "Shutdown command is ready."


def test_end_to_end_rejects_invalid_tool_arguments():

    result = process_ai_tool_call({
        "name": "file_exists",
        "arguments": {
            "file_path": 123
        }
    })

    assert result == "Argument 'file_path' must be a string."