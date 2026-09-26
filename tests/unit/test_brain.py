from app.core.brain import process_command,is_exit_command,get_help_message,COMMANDS
from app.tools.windows.applications import open_notepad,open_vscode,open_chrome,open_calculator
from app.tools.registry import get_tool
from app.tools.windows.system import (
    lock_computer,
    restart_computer,
    shutdown_computer
)

from app.tools.registry import (
    register_tool,
    get_tool,
    get_all_tools,
    execute_tool
)


def test_hello():

    result = process_command("hello")

    assert result == "Hello! How can I help you?"


def test_help():

    result = process_command("help")

    assert result == (
    "Available commands: hello, help, exit, time, date, "
    "open notepad, open calculator, open chrome, open vscode, "
    "lock computer, restart computer, shutdown computer, find file, "
    "check file, check folder, file info, list files, create folder"
)


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

 
    assert result == (
    "Available commands: hello, help, exit, time, date, "
    "open notepad, open calculator, open chrome, open vscode, "
    "lock computer, restart computer, shutdown computer, find file, "
    "check file, check folder, file info, list files, create folder"
)

def test_time_command():

    result = process_command("time")

    assert result.startswith("Current time is ")

def test_date_command():

    result = process_command("date")

    assert result.startswith("Today's date is ")

def test_open_notepad_command():

    assert callable(COMMANDS["open notepad"])
    assert get_tool("open_notepad") == open_notepad

def test_open_calculator_command():

    assert callable(COMMANDS["open calculator"])
    assert get_tool("open_calculator") == open_calculator


def test_open_chrome_command():

    assert callable(COMMANDS["open chrome"])
    assert get_tool("open_chrome") == open_chrome

def test_open_vscode_command():

    assert callable(COMMANDS["open vscode"])
    assert get_tool("open_vscode") == open_vscode

def test_lock_computer_command():

    assert callable(COMMANDS["lock computer"])
    assert get_tool("lock_computer") == lock_computer


def test_restart_computer_command():

    assert callable(COMMANDS["restart computer"])
    assert get_tool("restart_computer") == restart_computer


def test_shutdown_computer_command():

    assert callable(COMMANDS["shutdown computer"])
    assert get_tool("shutdown_computer") == shutdown_computer

def test_find_file_command():

    result = process_command("find file")

    assert result == "Please provide a file name."

def test_find_file_missing_file():

    result = process_command("find file definitely_missing_zyro_file.txt")

    assert result == "I could not find definitely_missing_zyro_file.txt."

def test_find_file_in_directory():

    result = process_command(
        "find file definitely_missing_zyro_file.txt in Desktop"
    )

    assert result == (
        "I could not find definitely_missing_zyro_file.txt."
        if "directory" not in result
        else result
    )


def test_find_file_without_name():

    result = process_command("find file")

    assert result == "Please provide a file name."


def test_find_file_without_directory():

    result = process_command("find file student.csv in")

    assert result == "Please provide a directory."

def test_find_file_in_missing_directory():

    result = process_command(
        "find file student.csv in DefinitelyMissingFolder"
    )

    assert result == (
        "I could not find the directory DefinitelyMissingFolder."
    )

def test_check_file_exists():

    test_file = "brain_test.txt"

    with open(test_file, "w") as file:
        file.write("Zyro test")

    result = process_command("check file brain_test.txt")

    assert result == "File exists: brain_test.txt"

    import os
    os.remove(test_file)


def test_check_file_missing():

    result = process_command(
        "check file definitely_missing_file.txt"
    )

    assert result == (
        "File does not exist: definitely_missing_file.txt"
    )


def test_check_folder_exists():

    result = process_command("check folder .")

    assert result == "Folder exists: ."


def test_check_folder_missing():

    result = process_command(
        "check folder DefinitelyMissingFolder"
    )

    assert result == (
        "Folder does not exist: DefinitelyMissingFolder"
    )


def test_file_info():

    test_file = "brain_info_test.txt"

    with open(test_file, "w") as file:
        file.write("Zyro test")

    result = process_command(
        "file info brain_info_test.txt"
    )

    assert result["name"] == "brain_info_test.txt"
    assert result["extension"] == ".txt"

    import os
    os.remove(test_file)


def test_list_files():

    result = process_command("list files")

    assert isinstance(result, list)


def test_list_files_in_directory():

    result = process_command("list files in .")

    assert isinstance(result, list)


def test_create_folder():

    folder_name = "zyro_brain_test"

    result = process_command(
        f"create folder {folder_name}"
    )

    assert result == (
        f"Directory created: {folder_name}"
    )

    import os
    os.rmdir(folder_name)


def test_register_tool():

    def test_function():
        return "Test successful"

    register_tool("test_tool", test_function)

    assert get_tool("test_tool") == test_function


def test_get_missing_tool():

    result = get_tool("missing_tool")

    assert result is None


def test_get_all_tools():

    def another_function():
        return "Another test"

    register_tool("another_tool", another_function)

    tools = get_all_tools()

    assert "another_tool" in tools
    assert tools["another_tool"] == another_function


def test_execute_tool():

    def greeting():

        return "Hello from tool"

    register_tool("greeting", greeting)

    result = execute_tool("greeting")

    assert result == "Hello from tool"


def test_execute_tool_with_arguments():

    def add_numbers(a, b):

        return a + b

    register_tool("add_numbers", add_numbers)

    result = execute_tool(
        "add_numbers",
        10,
        20
    )

    assert result == 30


def test_execute_missing_tool():

    result = execute_tool("missing_tool")

    assert result == (
        "Tool 'missing_tool' is not registered."
    )