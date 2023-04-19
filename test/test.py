from unittest.mock import patch
from ptb import funcs


def test_getextdata(tmp_path):

    file_to_write = tmp_path / "test"
    funcs.getexternaldata(file_to_write)

    content = file_to_write.open().read()

    assert len(content) > 50


@patch("ptb.funcs.requests.get")
@patch("ptb.funcs.requests.post")
def test_nodata(mock_post, mock_request, tmp_path):

    print(mock_request)
    print(type(mock_request))

    mock_request.return_value.text = "asdfasdf"
    
    file_to_write = tmp_path / "test"
    funcs.getexternaldata(file_to_write)

    content = file_to_write.open().read()

    assert content == "asdfasdf"
