import string
from pathlib import Path

import pytest

from dupeutil import console


DIR_NAME = "assets"
IMG_FILE_NAME = "dot.png"


def test_print_files():
    img_file = Path(__file__).parent / DIR_NAME / IMG_FILE_NAME
    original = img_file
    dupes = [img_file, img_file, img_file]
    assert console.print_files(original, dupes, 1, 1) == None


def test_prompt(monkeypatch):
    # When user presses Enter
    # Should return True
    monkeypatch.setattr("builtins.input", lambda _: "")
    assert console.prompt(5)

    # When user enters a y
    # Should return True
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert console.prompt(1)

    # When user enters a Y
    # Should return True
    monkeypatch.setattr("builtins.input", lambda _: "Y")
    assert console.prompt(1)

    # When user enters an n
    # Should return False
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert not console.prompt(1)

    # When user enters an N
    # Should return False
    monkeypatch.setattr("builtins.input", lambda _: "N")
    assert not console.prompt(1)


@pytest.mark.parametrize("char", string.printable)
def test_prompt_when_given_no_y_nor_n(char: str, monkeypatch):
    # When user enters a character other than a y or an n
    # Should return False
    if char.lower() == "y":
        assert True
    else:
        monkeypatch.setattr("builtins.input", lambda _: char)
        assert not console.prompt(1)


def test_print_table_part():
    # When given TablePart.BODY, Alignment.LEFT, and generic input
    # Should return None
    assert (
        console.print_table_part(
            console.TablePart.BODY, console.Alignment.LEFT, "input"
        )
        is None
    )

    # When given TablePart.HEAD, Alignment.CENTER, and generic input
    # Should return None
    assert (
        console.print_table_part(
            console.TablePart.HEAD, console.Alignment.CENTER, "input"
        )
        is None
    )

    # When given TablePart.FOOT, Alignment.RIGHT, and generic input
    # Should return None
    assert (
        console.print_table_part(
            console.TablePart.FOOT, console.Alignment.RIGHT, "input"
        )
        is None
    )

    # When given TablePart.BODY, Alignment.LEFT, generic input, and a fill char
    # Should return None
    assert (
        console.print_table_part(
            console.TablePart.BODY, console.Alignment.LEFT, "input", "-"
        )
        is None
    )

    # When given TablePart.BODY, Alignment.LEFT, generic input, a fill char, and padding
    # Should return None
    assert (
        console.print_table_part(
            console.TablePart.BODY, console.Alignment.LEFT, "input", "-", 5
        )
        is None
    )
