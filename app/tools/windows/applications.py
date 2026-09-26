import os
import shutil
import subprocess


APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": "chrome.exe",
    "vscode": "code.exe"
}


def find_application(application_name):

    application = APPLICATIONS.get(application_name)

    if not application:
        return None

    application_path = shutil.which(application)

    if application_path:
        return application_path

    return None


def open_application(application_name):

    application_path = find_application(application_name)

    if not application_path:
        return f"I could not find {application_name} on this computer."

    subprocess.Popen([application_path])

    return f"Opening {application_name}..."


def open_notepad():

    return open_application("notepad")


def open_calculator():

    return open_application("calculator")


def open_chrome():

    return open_application("chrome")


def open_vscode():

    return open_application("vscode")