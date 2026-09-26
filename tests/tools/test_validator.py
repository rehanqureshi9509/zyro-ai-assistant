from app.tools.validator import (
    validate_tool_metadata,
    validate_all_tools
)


def test_valid_tool_metadata():

    metadata = {
        "description": "Opens Google Chrome.",
        "parameters": {}
    }

    result = validate_tool_metadata(
        "open_chrome",
        metadata
    )

    assert result is True


def test_empty_tool_name():

    metadata = {
        "description": "Test tool.",
        "parameters": {}
    }

    result = validate_tool_metadata(
        "",
        metadata
    )

    assert result is False


def test_invalid_metadata_type():

    result = validate_tool_metadata(
        "test_tool",
        "invalid"
    )

    assert result is False


def test_missing_description():

    metadata = {
        "parameters": {}
    }

    result = validate_tool_metadata(
        "test_tool",
        metadata
    )

    assert result is False


def test_empty_description():

    metadata = {
        "description": "",
        "parameters": {}
    }

    result = validate_tool_metadata(
        "test_tool",
        metadata
    )

    assert result is False


def test_invalid_parameters_type():

    metadata = {
        "description": "Test tool.",
        "parameters": []
    }

    result = validate_tool_metadata(
        "test_tool",
        metadata
    )

    assert result is False


def test_invalid_parameter_name():

    metadata = {
        "description": "Test tool.",
        "parameters": {
            "": "str"
        }
    }

    result = validate_tool_metadata(
        "test_tool",
        metadata
    )

    assert result is False


def test_invalid_parameter_type():

    metadata = {
        "description": "Test tool.",
        "parameters": {
            "file_path": 123
        }
    }

    result = validate_tool_metadata(
        "test_tool",
        metadata
    )

    assert result is False



def test_validate_all_registered_tools():

    errors = validate_all_tools()

    assert errors == []