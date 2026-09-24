from datetime import datetime
from app.tools.windows.applications import open_notepad,open_calculator,open_chrome

HELLO_COMMAND = "hello"
HELP_COMMAND = "help"
EXIT_COMMAND = "exit"
TIME_COMMAND = "time"
DATE_COMMAND = "date"
OPEN_NOTEPAD_COMMAND = "open notepad"
OPEN_CALCULATOR_COMMAND = "open calculator"
OPEN_CHROME_COMMAND = "open chrome"


AVAILABLE_COMMANDS = [
    HELLO_COMMAND,
    HELP_COMMAND,
    EXIT_COMMAND,
    TIME_COMMAND,
    DATE_COMMAND,
    OPEN_NOTEPAD_COMMAND,
    OPEN_CALCULATOR_COMMAND,
    OPEN_CHROME_COMMAND
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


COMMANDS = {
    HELLO_COMMAND: handle_hello,
    HELP_COMMAND: handle_help,
    EXIT_COMMAND: handle_exit,
    TIME_COMMAND: handle_time,
    DATE_COMMAND: handle_date,
    OPEN_NOTEPAD_COMMAND: open_notepad,
    OPEN_CALCULATOR_COMMAND: open_calculator,
    OPEN_CHROME_COMMAND: open_chrome
}

def process_command(command):

    command = command.strip().lower()

    if not command:
        return "Please enter a command."

    handler = COMMANDS.get(command)

    if handler:
        return handler()

    return UNKNOWN_COMMAND_RESPONSE



def is_exit_command(command):

    command = command.strip().lower()

    return command == EXIT_COMMAND