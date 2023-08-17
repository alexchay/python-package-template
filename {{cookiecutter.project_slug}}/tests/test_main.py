import os
from unittest.mock import patch
from {{cookiecutter.project_slug}}.main import main


def test_main(capsys):
    """
    Test case for the main function.

    This test case mocks the 'ENVIRONMENT' environment variable and asserts that the main function
    prints the mocked value.
    """
    with patch.dict(os.environ, {"ENVIRONMENT": "test"}):
        main()
        captured = capsys.readouterr()
        assert "test" in captured.out

    with patch.dict(os.environ, {"ENVIRONMENT": "prod"}):
        main()
        captured = capsys.readouterr()
        assert "prod" in captured.out
