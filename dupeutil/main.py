import argparse
import pathlib
from collections import defaultdict

from . import console, core, utils


def main():
    namespace = parse_args()
    if namespace.version:
        from .__version__ import __version__

        print(__version__)
    elif namespace.dir:
        find_dupes_in_dir(namespace.dir, namespace.recursive, namespace.quiet)
    elif namespace.files:
        if len(namespace.files) < 2:
            raise TypeError("need at least two files to compare")

        find_dupes(namespace.files, namespace.quiet)
    else:
        find_dupes_in_dir(pathlib.Path.cwd(), namespace.recursive, namespace.quiet)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dir",
        nargs="?",
        type=str,
        help="the directory to check",
    )
    parser.add_argument(
        "-f",
        "--files",
        nargs="+",
        type=str,
        required=False,
        help="the files to compare",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        required=False,
        help="suppress output to the console; this option will not ask for permission to remove files",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        required=False,
        help="include files in subdirectories",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        required=False,
        help="print program version",
    )

    namespace = parser.parse_args()
    return namespace


def find_dupes_in_dir(dir: str, recursive: bool, quiet: bool):
    p = pathlib.Path(dir)
    if not p.is_dir():
        raise TypeError(f"'{p}' is not a path to a directory")

    if not p.exists():
        raise ValueError(f"'{p}' does not exist")

    files = [i for i in (p.rglob("*") if recursive else p.iterdir()) if i.is_file()]
    analyze_files(files, quiet)


def find_dupes(files: list, quiet: bool):
    file_paths = []
    for file in files:
        p = pathlib.Path(file)
        if not p.exists():
            raise ValueError(f"'{p}' does not exist")

        if p.is_dir():
            raise TypeError(f"'{p}' is a directory but was expecting a file")

        file_paths.append(p)

    analyze_files(file_paths, quiet)


def analyze_files(files: list, quiet: bool):
    # Prevents "picture - Copy.jpg" from appearing as the original before
    # "picture.jpg" when their modification/creation dates are the same
    files.sort(reverse=True)

    # Sorts files by their creation date or modified date (whichever is lowest)
    # from oldest to newest
    files.sort(key=lambda file: min(file.stat().st_ctime, file.stat().st_mtime))

    identical_files = core.filter_by_file_size(*files)
    identical_files = filter(core.are_files_equal, identical_files)
    dd = defaultdict(list)
    for original, dupe in identical_files:
        dd[original].append(dupe)

    total = len(dd)
    if total:
        for c, (original, dupes) in enumerate(dd.items(), 1):
            if quiet:
                for dupe in dupes:
                    dupe.unlink(True)
            else:
                len_dupes = len(dupes)
                console.print_files(original, dupes, c, total)
                success = console.prompt(len_dupes)
                if success:
                    for dupe in dupes:
                        dupe.unlink(True)

                    print(
                        f"Successfully removed {len_dupes} {utils.quantify(len_dupes, 'file')}\n"
                    )
                else:
                    print("No files were removed\n")
    elif not quiet:
        print(f"No duplicates were found")


if __name__ == "__main__":  # pragma: no cover
    main()
