from pathlib import Path

from app.tools.files.manager import (
    file_exists,
    directory_exists,
    get_file_info,
    create_directory,
    list_files
)


def test_file_exists():

    test_file = Path("test_file.txt")

    test_file.write_text("Zyro test")

    result = file_exists(test_file)

    assert result is True

    test_file.unlink()


def test_file_does_not_exist():

    result = file_exists("definitely_missing_file.txt")

    assert result is False


def test_directory_exists():

    result = directory_exists(".")

    assert result is True


def test_directory_does_not_exist():

    result = directory_exists("DefinitelyMissingFolder")

    assert result is False


def test_get_file_info():

    test_file = Path("test_info.txt")

    test_file.write_text("Hello Zyro")

    result = get_file_info(test_file)

    assert result["name"] == "test_info.txt"
    assert result["extension"] == ".txt"
    assert result["size"] > 0

    test_file.unlink()


def test_get_file_info_missing_file():

    result = get_file_info("definitely_missing_file.txt")

    assert result == (
        "I could not find definitely_missing_file.txt."
    )


def test_create_directory():

    directory = Path("zyro_test_folder")

    result = create_directory(directory)

    assert result == "Directory created: zyro_test_folder"
    assert directory.is_dir()

    directory.rmdir()


def test_list_files():

    directory = Path("zyro_list_test")

    directory.mkdir()

    file1 = directory / "file1.txt"
    file2 = directory / "file2.txt"

    file1.write_text("one")
    file2.write_text("two")

    result = list_files(directory)

    assert "file1.txt" in result
    assert "file2.txt" in result

    file1.unlink()
    file2.unlink()
    directory.rmdir()


def test_list_files_missing_directory():

    result = list_files("DefinitelyMissingFolder")

    assert result == (
        "I could not find the directory DefinitelyMissingFolder."
    )