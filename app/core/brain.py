def process_command(command):

    command = command.strip().lower()

    if not command:
        return "Please enter a command."

    if command == "hello":
        return "Hello! How can I help you?"

    elif command == "help":
        return "Available commands: hello, help, exit"

    elif command == "exit":
        return "Goodbye!"

    else:
        return "I don't understand that command yet."