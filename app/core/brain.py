from datetime import datetime

from app.tools.registry import execute_tool


HELLO_COMMAND = "hello"
HELP_COMMAND = "help"
EXIT_COMMAND = "exit"
TIME_COMMAND = "time"
DATE_COMMAND = "date"

OPEN_NOTEPAD_COMMAND = "open notepad"
OPEN_CALCULATOR_COMMAND = "open calculator"
OPEN_CHROME_COMMAND = "open chrome"
OPEN_VSCODE_COMMAND = "open vscode"

LOCK_COMMAND = "lock computer"
RESTART_COMMAND = "restart computer"
SHUTDOWN_COMMAND = "shutdown computer"

FIND_FILE_COMMAND = "find file"
IN_COMMAND = " in "

CHECK_FILE_COMMAND = "check file"
CHECK_FOLDER_COMMAND = "check folder"
FILE_INFO_COMMAND = "file info"
LIST_FILES_COMMAND = "list files"
CREATE_FOLDER_COMMAND = "create folder"


AVAILABLE_COMMANDS = [
    HELLO_COMMAND,
    HELP_COMMAND,
    EXIT_COMMAND,
    TIME_COMMAND,
    DATE_COMMAND,
    OPEN_NOTEPAD_COMMAND,
    OPEN_CALCULATOR_COMMAND,
    OPEN_CHROME_COMMAND,
    OPEN_VSCODE_COMMAND,
    LOCK_COMMAND,
    RESTART_COMMAND,
    SHUTDOWN_COMMAND,
    FIND_FILE_COMMAND,
    CHECK_FILE_COMMAND,
    CHECK_FOLDER_COMMAND,
    FILE_INFO_COMMAND,
    LIST_FILES_COMMAND,
    CREATE_FOLDER_COMMAND
]


UNKNOWN_COMMAND_RESPONSE = (
    "I don't understand that command yet. "
    "Type 'help' to see available commands."
)


def get_help_message():

    return "Available commands: " + ", ".join(AVAILABLE_COMMANDS)


def handle_hello():

    return "Hello! How can I help you?"


def handle_help():

    return get_help_message()


def handle_exit():

    return "Goodbye!"


def handle_time():

    current_time = datetime.now()

    return current_time.strftime("Current time is %I:%M %p")


def handle_date():

    current_date = datetime.now()

    return current_date.strftime("Today's date is %d %B %Y")


def handle_find_file(command):

    search_text = command[len(FIND_FILE_COMMAND):].strip()

    if not search_text:

        return "Please provide a file name."

    if search_text.lower().endswith(" in"):

        file_name = search_text[:-3].strip()

        if not file_name:

            return "Please provide a file name."

        return "Please provide a directory."

    if IN_COMMAND in search_text.lower():

        in_position = search_text.lower().find(IN_COMMAND)

        file_name = search_text[:in_position].strip()

        search_directory = search_text[
            in_position + len(IN_COMMAND):
        ].strip()

        if not file_name:

            return "Please provide a file name."

        if not search_directory:

            return "Please provide a directory."

        return execute_tool(
            "search_file",
            file_name,
            search_directory
        )

    return execute_tool(
        "search_file",
        search_text
    )


def handle_check_file(command):

    file_path = command[len(CHECK_FILE_COMMAND):].strip()

    if not file_path:

        return "Please provide a file path."

    result = execute_tool(
        "file_exists",
        file_path
    )

    if result:

        return f"File exists: {file_path}"

    return f"File does not exist: {file_path}"


def handle_check_folder(command):

    folder_path = command[len(CHECK_FOLDER_COMMAND):].strip()

    if not folder_path:

        return "Please provide a folder path."

    result = execute_tool(
        "directory_exists",
        folder_path
    )

    if result:

        return f"Folder exists: {folder_path}"

    return f"Folder does not exist: {folder_path}"


def handle_file_info(command):

    file_path = command[len(FILE_INFO_COMMAND):].strip()

    if not file_path:

        return "Please provide a file path."

    return execute_tool(
        "get_file_info",
        file_path
    )


def handle_list_files(command):

    search_directory = command[len(LIST_FILES_COMMAND):].strip()

    if not search_directory:

        return execute_tool(
            "list_files"
        )

    if not search_directory.startswith("in "):

        return "Use: list files or list files in <directory>."

    directory_path = search_directory[3:].strip()

    if not directory_path:

        return "Please provide a directory."

    return execute_tool(
        "list_files",
        directory_path
    )


def handle_create_folder(command):

    folder_path = command[len(CREATE_FOLDER_COMMAND):].strip()

    if not folder_path:

        return "Please provide a folder path."

    return execute_tool(
        "create_directory",
        folder_path
    )


COMMANDS = {
    HELLO_COMMAND: handle_hello,
    HELP_COMMAND: handle_help,
    EXIT_COMMAND: handle_exit,
    TIME_COMMAND: handle_time,
    DATE_COMMAND: handle_date,

    OPEN_NOTEPAD_COMMAND: lambda: execute_tool(
        "open_notepad"
    ),

    OPEN_CALCULATOR_COMMAND: lambda: execute_tool(
        "open_calculator"
    ),

    OPEN_CHROME_COMMAND: lambda: execute_tool(
        "open_chrome"
    ),

    OPEN_VSCODE_COMMAND: lambda: execute_tool(
        "open_vscode"
    ),

    LOCK_COMMAND: lambda: execute_tool(
        "lock_computer"
    ),

    RESTART_COMMAND: lambda: execute_tool(
        "restart_computer"
    ),

    SHUTDOWN_COMMAND: lambda: execute_tool(
        "shutdown_computer"
    )
}


def process_command(command):

    original_command = command.strip()

    normalized_command = original_command.lower()

    if not original_command:

        return "Please enter a command."

    if normalized_command == FIND_FILE_COMMAND:

        return "Please provide a file name."

    if normalized_command.startswith(FIND_FILE_COMMAND + " "):

        return handle_find_file(original_command)

    if normalized_command == CHECK_FILE_COMMAND:

        return "Please provide a file path."

    if normalized_command.startswith(CHECK_FILE_COMMAND + " "):

        return handle_check_file(original_command)

    if normalized_command == CHECK_FOLDER_COMMAND:

        return "Please provide a folder path."

    if normalized_command.startswith(CHECK_FOLDER_COMMAND + " "):

        return handle_check_folder(original_command)

    if normalized_command == FILE_INFO_COMMAND:

        return "Please provide a file path."

    if normalized_command.startswith(FILE_INFO_COMMAND + " "):

        return handle_file_info(original_command)

    if normalized_command == LIST_FILES_COMMAND:

        return handle_list_files(original_command)

    if normalized_command.startswith(LIST_FILES_COMMAND + " "):

        return handle_list_files(original_command)

    if normalized_command == CREATE_FOLDER_COMMAND:

        return "Please provide a folder path."

    if normalized_command.startswith(CREATE_FOLDER_COMMAND + " "):

        return handle_create_folder(original_command)

    handler = COMMANDS.get(normalized_command)

    if handler:

        return handler()

    return UNKNOWN_COMMAND_RESPONSE


def is_exit_command(command):

    command = command.strip().lower()

    return command == EXIT_COMMAND