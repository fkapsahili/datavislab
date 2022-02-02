from pathlib import Path
import os


def find_file(fn_str):
    """Attempts to find file relative to cwd.
       If not found, steps up into parent directory.
       After third failed attempt to find file in parent dir,
       returns None.

    Args:
        fn_str (str): file name of file to find.

    Returns:
        str: path relative to cwd as str or None
    """
    max_attempts = 3
    attempts = 0
    while True:
        try:
            lpath = next(Path(".").rglob(fn_str)).as_posix()
            print(f"found {lpath}")
            return lpath
        except StopIteration:
            pass
        print(f"Couldn't find {fn_str} relative to {os.getcwd()}")
        if attempts == max_attempts:
            return None
        os.chdir("..")
        attempts += 1
        print(f"attempting within: {os.getcwd()}")
