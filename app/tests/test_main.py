import sys

import pytest
from pytest import CaptureFixture, MonkeyPatch
from pytest_mock import MockerFixture

from app.__main__ import Args, main, parse_args


@pytest.mark.parametrize(
    "argv, expected",
    [
        (["app", "--name", "World"], "World"),
        (["app", "--name", "Alice"], "Alice"),
    ],
)
def test_parse_args(monkeypatch: MonkeyPatch, argv: list[str], expected: str):
    monkeypatch.setattr(sys, "argv", argv)
    args = parse_args()
    assert args.name == expected


def test_main(mocker: MockerFixture, capsys: CaptureFixture[str]):
    mock_greet = mocker.patch("app.__main__.greet")
    mock_greet.return_value = "Hello, World!"

    args = Args()
    args.name = "World"

    main(args)

    captured = capsys.readouterr()

    mock_greet.assert_called_once_with("World")
    assert captured.out.strip() == "Hello, World!"
