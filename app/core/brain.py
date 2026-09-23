def process_command(command):

    if not command:
        return "Please enter a command."

    return handle_command(command)


def handle_command(command):

    command = command.strip().lower()

    if command == "hello":
        return "Hello! How can I help you?"

    elif command == "help":
        return "Available commands: hello, help, exit"

    elif command == "exit":
        return "Goodbye!"

    else:
        return "I don't understand that command yet."