import pathlib

from . import utils


def filter_by_file_size(*files: tuple) -> list:
    # {int: pathlib.Path}
    file_sizes = {}

    # [(pathlib.Path, pathlib.Path)]
    identical_files = []
    for file in files:
        file_size = file.stat().st_size

        # Checks if an identical file size has already been encountered
        value_file = file_sizes.get(file_size)
        if value_file:
            # Appends in order of oldest creation date to newest
            identical_files.append((value_file, file))
        else:
            file_sizes[file_size] = file

    return identical_files


def are_files_equal(*files: tuple) -> bool:
    for f1, f2 in files:
        return (
            utils.get_hexdigest(f1, 1024) == utils.get_hexdigest(f2, 1024)
            and utils.get_hexdigest(f1) == utils.get_hexdigest(f2)
            and utils.cmp_bytes(f1, f2)
        )
