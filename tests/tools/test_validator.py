from app.tools.validator import (
    validate_tool_metadata,
    validate_all_tools,
    validate_tool_schema,
    validate_tool_registry
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


def test_all_registered_tool_schemas_are_valid():

    errors = validate_tool_registry()

    assert errors == []


def test_file_exists_schema_is_valid():

    errors = validate_tool_schema("file_exists")

    assert errors == []


def test_search_file_schema_is_valid():

    errors = validate_tool_schema("search_file")

    assert errors == []


def test_registry_contains_unique_tool_names():

    from app.tools.registry import get_all_tools

    tools = get_all_tools()

    assert len(tools) > 0
    assert len(set(tools)) == len(tools)