HELLO_COMMAND = "hello"
HELP_COMMAND = "help"
EXIT_COMMAND = "exit"


AVAILABLE_COMMANDS = [
    HELLO_COMMAND,
    HELP_COMMAND,
    EXIT_COMMAND
]


def process_command(command):

    command = command.strip().lower()

    if not command:
        return "Please enter a command."

    return handle_command(command)


def handle_command(command):

    if command == HELLO_COMMAND:
        return "Hello! How can I help you?"

    elif command == HELP_COMMAND:
        return "Available commands: hello, help, exit"

    elif command == EXIT_COMMAND:
        return "Goodbye!"

    else:
        return "I don't understand that command yet."

def get_help_message():

    return "Available commands: " + ", ".join(AVAILABLE_COMMANDS)

def is_exit_command(command):

    command = command.strip().lower()

    return command == EXIT_COMMAND