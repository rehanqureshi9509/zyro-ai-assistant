from pathlib import Path


def search_file(file_name, search_directory="."):

    search_path = Path(search_directory)

    if not search_path.exists():

        return f"I could not find the directory {search_directory}."

    for file_path in search_path.rglob(file_name):

        if file_path.is_file():

            return str(file_path.resolve())

    return f"I could not find {file_name}."