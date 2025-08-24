import pytest

from app.utils.greet import greet


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
    ],
)
def test_greet(name: str, expected: str):
    assert greet(name) == expected
