from app.core.brain import process_command


def test_hello():

    result = process_command("hello")

    assert result == "Hello! How can I help you?"


def test_help():

    result = process_command("help")

    assert result == "Available commands: hello, help, exit"


def test_exit():

    result = process_command("exit")

    assert result == "Goodbye!"


def test_empty_command():

    result = process_command("")

    assert result == "Please enter a command."


def test_unknown_command():

    result = process_command("xyz")

    assert result == "I don't understand that command yet."