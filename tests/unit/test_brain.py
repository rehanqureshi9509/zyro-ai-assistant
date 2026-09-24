from app.core.brain import process_command,is_exit_command,get_help_message


def test_hello():

    result = process_command("hello")

    assert result == "Hello! How can I help you?"


def test_help():

    result = process_command("help")

    assert result == "Available commands: hello, help, exit, time, date"


def test_exit():

    result = process_command("exit")

    assert result == "Goodbye!"


def test_empty_command():

    result = process_command("")

    assert result == "Please enter a command."


def test_unknown_command():

    result = process_command("xyz")

    assert result == (
        "I don't understand that command yet. "
        "Type 'help' to see available commands."
    )

def test_hello_uppercase():

    result = process_command("HELLO")

    assert result == "Hello! How can I help you?"


def test_hello_mixed_case():

    result = process_command("HeLLo")

    assert result == "Hello! How can I help you?"


def test_hello_with_spaces():

    result = process_command("   hello   ")

    assert result == "Hello! How can I help you?"


def test_exit_command():

    result = is_exit_command("exit")

    assert result is True


def test_exit_command_uppercase():

    result = is_exit_command("EXIT")

    assert result is True


def test_exit_command_with_spaces():

    result = is_exit_command("   exit   ")

    assert result is True


def test_not_exit_command():

    result = is_exit_command("hello")

    assert result is False

def test_help_message():

    result = get_help_message()

    assert result == "Available commands: hello, help, exit, time, date"

def test_time_command():

    result = process_command("time")

    assert result.startswith("Current time is ")

def test_date_command():

    result = process_command("date")

    assert result.startswith("Today's date is ")