import shutil
from datetime import datetime
from enum import auto, Enum
from pathlib import Path

from . import utils


TABLEPART_UNICODE_CODE_POINT_DIFF = 4


class TablePart(Enum):
    HEAD = 9487
    BODY = 9475
    FOOT = 9495


class Alignment(Enum):
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()


def print_files(original: Path, dupes: list, pos: int, total: int):
    print_table_part(
        TablePart.HEAD, Alignment.CENTER, f"Original ({pos}/{total})", "━", 1
    )

    dt = datetime.fromtimestamp(original.stat().st_ctime)
    print_table_part(TablePart.BODY, Alignment.CENTER, str(original))
    print_table_part(TablePart.BODY, Alignment.CENTER, str(dt.strftime("%x @ %X")))
    print_table_part(TablePart.BODY, Alignment.CENTER, "")

    print_table_part(TablePart.BODY, Alignment.CENTER, "Duplicates:")
    for c, dupe in enumerate(dupes, 1):
        n = f"{c}. "
        print_table_part(TablePart.BODY, Alignment.LEFT, f"{n}{dupe}")
        dt = datetime.fromtimestamp(dupe.stat().st_ctime)
        print_table_part(
            TablePart.BODY,
            Alignment.LEFT,
            f"└─{dt.strftime('%x @ %X')}",
            padding=len(n),
        )

    print_table_part(TablePart.FOOT, Alignment.CENTER, "", "━")


def prompt(total: int) -> bool:
    r = input(
        f"Remove {utils.quantify(total, 'this file', 'these files')}? (y/N)\n>>> "
    )
    return r.lower() == "y" or r == ""


def print_table_part(
    part: TablePart,
    alignment: Alignment,
    input: str,
    fillchar: str = " ",
    padding: int = 0,
):
    if part == TablePart.BODY:
        left_side = right_side = chr(part.value)
    else:
        left_side = chr(part.value)
        right_side = chr(part.value + TABLEPART_UNICODE_CODE_POINT_DIFF)

    width = shutil.get_terminal_size()[0]
    diff = width - len(left_side) - len(right_side)
    padded_input = input.center(len(input) + padding * 2, " ")

    if alignment == Alignment.LEFT:
        aligned_input = padded_input.ljust(diff, fillchar)
    elif alignment == Alignment.CENTER:
        aligned_input = padded_input.center(diff, fillchar)
    elif alignment == Alignment.RIGHT:
        aligned_input = padded_input.rjust(diff, fillchar)

    print(left_side + aligned_input + right_side)
