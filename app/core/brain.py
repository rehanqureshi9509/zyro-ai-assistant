HELLO_COMMAND = "hello"
HELP_COMMAND = "help"
EXIT_COMMAND = "exit"


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