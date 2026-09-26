# app/core/permissions.py

CONFIRMATION_REQUIRED_TOOLS = {
    "lock_computer",
    "restart_computer",
    "shutdown_computer",
}


def requires_confirmation(tool_name):

    return tool_name in CONFIRMATION_REQUIRED_TOOLS


def check_tool_permission(tool_name, confirmed=False):

    if requires_confirmation(tool_name) and not confirmed:
        return False, (
            f"Confirmation required to execute '{tool_name}'."
        )

    return True, "Permission granted."