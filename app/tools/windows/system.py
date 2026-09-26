import subprocess


def lock_computer():

    subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])

    return "Locking the computer..."


def restart_computer():

    return "Restart command is ready."


def shutdown_computer():

    return "Shutdown command is ready."