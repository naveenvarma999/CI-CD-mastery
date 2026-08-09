from greeting import greet


def test_greet(capsys):
    greet("Prasu")

    captured = capsys.readouterr()

    assert captured.out == "Hello Prasu\n"


def test_uppercase():
    assert "hello".upper() == "HELLO"


def test_list_length():
    numbers = [10, 20, 30]

    assert len(numbers) == 3


def test_item_in_list():
    fruits = ["apple", "banana", "orange"]

    assert "banana" in fruits