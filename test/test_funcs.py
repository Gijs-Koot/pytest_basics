import pytest

from ptb import funcs


def test_badsum():

    assert funcs.badsum(1, 3) == 4


def test_writefile_fileexists(tmp_path):

    # create file first
    tmp_file_exists = tmp_path / "test"
    with tmp_file_exists.open("w") as f:
        f.write("adasdf")

    with pytest.raises(ValueError):
        funcs.writefile([1, 2, 3, 4], tmp_file_exists)


def test_writefile_normal(tmp_path):

    tmp_file = tmp_path / "test"

    funcs.writefile([1, -2, 300000], tmp_file)

    lines = [l for l in tmp_file.open()]

    assert lines == ["1\n", "-2\n", "300000\n"]

def test_with_tmppath(tmp_path):
    
    # setup temp file

    print(tmp_path)
    
    with (tmp_path / "test").open("w") as f:
        f.write("Hello 123!")

def test_sqrt():

    assert funcs.calc_square_root(2.) == pytest.approx(1.4142, abs=0.0001)


def test_badsum_with_fixture(correct_sums):

    for a, b, c in correct_sums:
        assert funcs.badsum(a, b) == c, f"{a} and {b} makes {c}!"
    