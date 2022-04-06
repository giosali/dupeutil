import pathlib

import pytest

from dupeutil import console, main, __version__


DIR_NAME = "assets"
IMG_FILE_NAME = "dot.png"
LARGER_IMG_FILE_NAME = "larger_dot.png"


class DotDict(dict):
    """dot.notation access to dictionary attributes"""

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def test_main(monkeypatch):
    # When passed -v
    # Should return None
    d = {"version": __version__}
    monkeypatch.setattr(main, "parse_args", lambda: DotDict(d))
    assert main.main() is None

    # When passed a directory
    # Should return None
    d = {"dir": True}
    monkeypatch.setattr(main, "parse_args", lambda: DotDict(d))
    monkeypatch.setattr(main, "find_dupes_in_dir", generic_args)
    assert main.main() is None

    # When passed files
    # Should return None
    d = {"files": [1, 2]}
    monkeypatch.setattr(main, "parse_args", lambda: DotDict(d))
    monkeypatch.setattr(main, "find_dupes", generic_args)
    assert main.main() is None

    # When passed less than two files
    # Should throw TypeError
    d = {"files": [1]}
    monkeypatch.setattr(main, "parse_args", lambda: DotDict(d))
    with pytest.raises(TypeError):
        assert main.main() is None

    # When passed nothing
    # Should return None
    d = {}
    monkeypatch.setattr(main, "parse_args", lambda: DotDict(d))
    assert main.main() is None


def test_find_dupes_in_dir(monkeypatch):
    img_file = pathlib.Path(__file__).parent / DIR_NAME / IMG_FILE_NAME
    nonexistent_dir = pathlib.Path(__file__).parent / "bassets"
    real_dir = pathlib.Path(__file__).parent

    # When given a file instead of a dir
    # Should throw TypeError
    with pytest.raises(TypeError):
        main.find_dupes_in_dir(str(img_file), False, False)

    # When given a nonexistent dir
    # Should throw TypeError
    with pytest.raises(TypeError):
        main.find_dupes_in_dir(str(nonexistent_dir), False, False)

    # When given a real dir
    # Should return None
    monkeypatch.setattr(main, "analyze_files", generic_args)
    assert main.find_dupes_in_dir(str(real_dir), False, False) is None

    # When given a real dir and recursive is True
    # Should return None
    assert main.find_dupes_in_dir(str(real_dir), True, False) is None


def test_find_dupes(monkeypatch):
    nonexistent_file = pathlib.Path(__file__).parent / DIR_NAME / "nonexistent.jpg"
    real_dir = pathlib.Path(__file__).parent
    real_file = pathlib.Path(__file__).parent / DIR_NAME / IMG_FILE_NAME

    # When given nonexistent file
    # Should throw ValueError
    with pytest.raises(ValueError):
        main.find_dupes([nonexistent_file], False)

    # When given dir
    # Should throw TypeError
    with pytest.raises(TypeError):
        main.find_dupes([real_dir], False)

    # When given real file
    # Should return None
    monkeypatch.setattr(main, "analyze_files", generic_args)
    assert main.find_dupes([real_file], False) is None


def test_analyze_files(monkeypatch):
    img_file = pathlib.Path(__file__).parent / DIR_NAME / IMG_FILE_NAME
    monkeypatch.setattr(pathlib.Path, "unlink", generic_args)
    monkeypatch.setattr(console, "print_files", generic_args)

    # When given empty list of files
    # Should return None
    files = []
    assert main.analyze_files(files, False) is None

    # When given files and enter y to remove
    # Should return None
    files = [img_file, img_file]
    monkeypatch.setattr(console, "prompt", lambda _: True)
    assert main.analyze_files(files, False) is None

    # When given files and enter n to remove
    # Should return None
    monkeypatch.setattr(console, "prompt", lambda _: False)
    assert main.analyze_files(files, False) is None

    # When given files, enter y to remove, and quiet is True
    # Should return None
    files = [img_file, img_file]
    monkeypatch.setattr(console, "prompt", lambda _: True)
    assert main.analyze_files(files, True) is None

    # When given files, enter n to remove, and quiet is True
    # Should return None
    monkeypatch.setattr(console, "prompt", lambda _: False)
    assert main.analyze_files(files, True) is None


def generic_args(*_):
    pass
