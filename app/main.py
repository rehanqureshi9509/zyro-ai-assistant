from app.core.brain import process_command


def start_zyro():

    print("Zyro is starting...")

    while True:

        command = input("You: ")

        response = process_command(command)

        print("Zyro:", response)

        if command.strip().lower() == "exit":
            break