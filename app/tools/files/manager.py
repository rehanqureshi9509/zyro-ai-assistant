from pathlib import Path


def file_exists(file_path):

    path = Path(file_path)

    return path.is_file()


def directory_exists(directory_path):

    path = Path(directory_path)

    return path.is_dir()


def get_file_info(file_path):

    path = Path(file_path)

    if not path.is_file():
        return f"I could not find {file_path}."

    return {
        "name": path.name,
        "extension": path.suffix,
        "size": path.stat().st_size,
        "path": str(path.resolve())
    }


def create_directory(directory_path):

    path = Path(directory_path)

    path.mkdir(parents=True, exist_ok=True)

    return f"Directory created: {directory_path}"


def list_files(directory_path="."):

    path = Path(directory_path)

    if not path.is_dir():
        return f"I could not find the directory {directory_path}."

    files = []

    for item in path.iterdir():

        if item.is_file():
            files.append(item.name)

    return files