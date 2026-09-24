import os
import subprocess


APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
}


def open_application(application_name):

    application = APPLICATIONS.get(application_name)

    if not application:
        return f"I don't know how to open {application_name}."

    if not os.path.exists(application) and application_name == "chrome":
        return "Chrome executable was not found."

    subprocess.Popen([application])

    return f"Opening {application_name}..."


def open_notepad():

    return open_application("notepad")


def open_calculator():

    return open_application("calculator")


def open_chrome():

    return open_application("chrome")