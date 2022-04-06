import pathlib

import pytest

from dupeutil import utils


DIR_NAME = "assets"
IMG_FILE_NAME = "dot.png"
LARGER_IMG_FILE_NAME = "larger_dot.png"

test_quantify_testdata = [
    (0, "item", "items", "items"),
    (1, "item", "items", "item"),
    (2, "item", "items", "items"),
    (0, "this file", "those files", "those files"),
    (1, "this file", "those files", "this file"),
    (2, "this file", "those files", "those files"),
]

test_quantify_no_plural_testdata = [
    (0, "item", "items"),
    (1, "item", "item"),
    (2, "item", "items"),
    (0, "this file", "this files"),
    (1, "this file", "this file"),
    (2, "this file", "this files"),
]


def test_get_hexdigest():
    # When given nonexistent file
    # Should throw FileNotFoundError
    nonexistent_file = r"C:\U\D\f.nonexistent"
    with pytest.raises(FileNotFoundError):
        _ = utils.get_hexdigest(nonexistent_file)

    # When given valid file
    # Should return str
    img_file = pathlib.Path(__file__).parent / DIR_NAME / IMG_FILE_NAME
    assert isinstance(utils.get_hexdigest(img_file), str)

    # When given valid file and size
    # Should return str
    assert isinstance(utils.get_hexdigest(img_file, 1024), str)

    # When executed twice on same file
    # Should return same str
    s1 = utils.get_hexdigest(img_file)
    s2 = utils.get_hexdigest(img_file)
    assert s1 == s2


def test_cmp_bytes():
    img_file = pathlib.Path(__file__).parent / DIR_NAME / IMG_FILE_NAME

    # When given a nonexistent file
    # Should throw FileNotFoundError
    nonexistent_file = r"C:\U\D\f.nonexistent"
    with pytest.raises(FileNotFoundError):
        _ = utils.cmp_bytes(nonexistent_file, img_file)

    with pytest.raises(FileNotFoundError):
        _ = utils.cmp_bytes(img_file, nonexistent_file)

    # When given valid files
    # Should return bool
    assert isinstance(utils.cmp_bytes(img_file, img_file), bool)

    # When given two of the same file
    # Should return True
    assert utils.cmp_bytes(img_file, img_file)

    # When given two different files
    # Should return True
    larger_img_file = pathlib.Path(__file__).parent / DIR_NAME / LARGER_IMG_FILE_NAME
    assert not utils.cmp_bytes(img_file, larger_img_file)


@pytest.mark.parametrize("count,singular,plural,expected", test_quantify_testdata)
def test_quantify(count: int, singular: str, plural: str, expected: str):
    assert expected == utils.quantify(count, singular, plural)


@pytest.mark.parametrize("count,singular,expected", test_quantify_no_plural_testdata)
def test_quantify_no_plural(count: int, singular: str, expected: str):
    assert expected == utils.quantify(count, singular)
