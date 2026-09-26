
from app.tools.registry import register_tool
from app.tools.executor import execute_tool


# 1. Execute a registered tool

def test_execute_registered_tool():

    def greeting():
        return "Hello from Zyro"

    register_tool(
        "executor_greeting",
        greeting,
        {
            "description": "Returns a greeting.",
            "parameters": {}
        }
    )

    result = execute_tool("executor_greeting")

    assert result == "Hello from Zyro"


# 2. Execute a tool with arguments

def test_execute_tool_with_arguments():

    def add_numbers(a, b):
        return a + b

    register_tool(
        "executor_add",
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
        "executor_add",
        10,
        20
    )

    assert result == 30


# 3. Execute a missing tool

def test_execute_missing_tool():

    result = execute_tool("unknown_executor_tool")

    assert result == (
        "Tool 'unknown_executor_tool' is not registered."
    )


# 4. Handle tool execution errors

def test_execute_tool_with_error():

    def faulty_tool():
        raise ValueError("Something went wrong")

    register_tool(
        "executor_faulty",
        faulty_tool,
        {
            "description": "Test tool that raises an error.",
            "parameters": {}
        }
    )

    result = execute_tool("executor_faulty")

    assert result == (
        "Error executing tool 'executor_faulty': "
        "Something went wrong"
    )


# 5. Reject a non-callable registered object

def test_execute_non_callable_tool():

    register_tool(
        "executor_invalid",
        "not a function",
        {
            "description": "Invalid test tool.",
            "parameters": {}
        }
    )

    result = execute_tool("executor_invalid")

    assert result == (
        "Tool 'executor_invalid' cannot be executed."
    )


# 6. Registry delegates execution to executor

def test_registry_execute_tool():

    from app.tools.registry import execute_tool as registry_execute

    def test_function():
        return "Registry delegation works"

    register_tool(
        "executor_registry_test",
        test_function,
        {
            "description": "Tests registry delegation.",
            "parameters": {}
        }
    )

    result = registry_execute("executor_registry_test")

    assert result == "Registry delegation works"