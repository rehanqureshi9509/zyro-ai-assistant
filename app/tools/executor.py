
from app.tools.registry import get_tool


def execute_tool(name, *args, **kwargs):
    """
    Executes a registered Zyro tool by its name.
    """

    tool = get_tool(name)

    # Check whether the tool exists
    if tool is None:
        return f"Tool '{name}' is not registered."

    # Check whether the registered object is callable
    if not callable(tool):
        return f"Tool '{name}' cannot be executed."

    # Execute the tool safely
    try:
        result = tool(*args, **kwargs)

        return result

    except Exception as error:
        return (
            f"Error executing tool '{name}': "
            f"{error}"
        )