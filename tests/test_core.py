import pathlib

from dupeutil import core


DIR_NAME = "assets"
IMG_FILE_NAME = "dot.png"
LARGER_IMG_FILE_NAME = "larger_dot.png"


def test_filter_by_file_size():
    img_file = pathlib.Path(__file__).parent / DIR_NAME / IMG_FILE_NAME
    larger_img_file = pathlib.Path(__file__).parent / DIR_NAME / LARGER_IMG_FILE_NAME

    # When given a list of two identical files
    # Should return a list of a tuple of those identical files
    files = [img_file, img_file]
    assert core.filter_by_file_size(*files) == [(img_file, img_file)]

    # When given a list of two different files
    # Should return an empty list
    files = [img_file, larger_img_file]
    assert core.filter_by_file_size(*files) == []


def test_are_files_equal():
    img_file = pathlib.Path(__file__).parent / DIR_NAME / IMG_FILE_NAME
    larger_img_file = pathlib.Path(__file__).parent / DIR_NAME / LARGER_IMG_FILE_NAME

    # When given a list of two identical files
    # Should return True
    files = [img_file, img_file]
    assert core.are_files_equal(files)

    # When given a list of two different files
    # Should return False
    files = [img_file, larger_img_file]
    assert not core.are_files_equal(files)
