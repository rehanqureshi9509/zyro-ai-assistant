from app.core.brain import process_command, is_exit_command


def start_zyro():

    print("Zyro is starting...")

    while True:

        command = input("You: ")

        response = process_command(command)

        print("Zyro:", response)

        if is_exit_command(command):
            break


# git command 

# cd ~/Desktop/"zyro ai assistant"
# source venv/Scripts/activate