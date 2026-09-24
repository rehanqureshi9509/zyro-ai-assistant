import subprocess


def open_notepad():
    subprocess.Popen(["notepad.exe"])

    return "Opening Notepad..."