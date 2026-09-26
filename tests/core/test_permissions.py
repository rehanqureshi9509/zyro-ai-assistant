from app.core.permissions import (
    requires_confirmation,
    check_tool_permission
)


def test_normal_tool_does_not_require_confirmation():

    assert requires_confirmation("open_notepad") is False


def test_system_tool_requires_confirmation():

    assert requires_confirmation("shutdown_computer") is True


def test_normal_tool_permission_granted():

    allowed, message = check_tool_permission("open_chrome")

    assert allowed is True
    assert message == "Permission granted."


def test_system_tool_permission_denied_without_confirmation():

    allowed, message = check_tool_permission("shutdown_computer")

    assert allowed is False
    assert message == (
        "Confirmation required to execute 'shutdown_computer'."
    )


def test_system_tool_permission_granted_with_confirmation():

    allowed, message = check_tool_permission(
        "shutdown_computer",
        confirmed=True
    )

    assert allowed is True
    assert message == "Permission granted."