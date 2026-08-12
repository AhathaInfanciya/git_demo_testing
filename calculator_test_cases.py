import pytest

from unittest.mock import patch

from calculator import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
)

# ─── add_numbers ───────────────────────────────────────────


def test_add_positive_numbers():

    assert add_numbers(10, 5) == 15


def test_add_negative_numbers():

    assert add_numbers(-10, -5) == -15


def test_add_zero():

    assert add_numbers(0, 5) == 5


def test_add_both_zero():

    assert add_numbers(0, 0) == 0


def test_add_floats():

    assert add_numbers(1.5, 2.5) == 4.0


def test_add_large_numbers():

    assert add_numbers(999999, 999999) == 1999998


def test_add_negative_and_positive():

    assert add_numbers(-5, 10) == 5


# ─── subtract_numbers ──────────────────────────────────────


def test_subtract_positive_numbers():

    assert subtract_numbers(10, 5) == 5


def test_subtract_negative_result():

    assert subtract_numbers(5, 10) == -5


def test_subtract_zero():

    assert subtract_numbers(5, 0) == 5


def test_subtract_same_numbers():

    assert subtract_numbers(5, 5) == 0


def test_subtract_floats():

    assert subtract_numbers(10.5, 0.5) == 10.0


def test_subtract_negative_numbers():

    assert subtract_numbers(-10, -5) == -5


def test_subtract_large_numbers():

    assert subtract_numbers(999999, 1) == 999998


# ─── multiply_numbers ──────────────────────────────────────


def test_multiply_positive_numbers():

    assert multiply_numbers(10, 5) == 50


def test_multiply_by_zero():

    assert multiply_numbers(10, 0) == 0


def test_multiply_by_one():

    assert multiply_numbers(5, 1) == 5


def test_multiply_negative_numbers():

    assert multiply_numbers(-3, 4) == -12


def test_multiply_floats():

    assert multiply_numbers(2.5, 4) == 10.0


def test_multiply_both_negative():

    assert multiply_numbers(-3, -4) == 12


def test_multiply_large_numbers():

    assert multiply_numbers(1000, 1000) == 1000000


# ─── divide_numbers ────────────────────────────────────────


def test_divide_positive_numbers():

    assert divide_numbers(10, 5) == 2.0


def test_divide_negative_numbers():

    assert divide_numbers(-10, 2) == -5.0


def test_divide_by_negative():

    assert divide_numbers(10, -2) == -5.0


def test_divide_zero_by_number():

    assert divide_numbers(0, 5) == 0.0


def test_divide_float_result():

    assert divide_numbers(10, 3) == pytest.approx(3.333, rel=1e-3)


def test_divide_by_zero_returns_string():

    assert divide_numbers(10, 0) == "Error: Division by zero"


def test_divide_by_zero_return_type():

    result = divide_numbers(10, 0)

    assert isinstance(result, str)


def test_divide_floats():

    assert divide_numbers(7.5, 2.5) == 3.0


def test_divide_large_numbers():

    assert divide_numbers(1000000, 1000) == 1000.0


# ─── main() full flow ──────────────────────────────────────


def test_main_addition(capsys):

    with patch("builtins.input", side_effect=["10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: 15" in captured.out


def test_main_subtraction(capsys):

    with patch("builtins.input", side_effect=["10", "5", "-"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: 5" in captured.out


def test_main_multiplication(capsys):

    with patch("builtins.input", side_effect=["10", "5", "*"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: 50" in captured.out


def test_main_division(capsys):

    with patch("builtins.input", side_effect=["10", "5", "/"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: 2" in captured.out


# ─── main() float input ────────────────────────────────────


def test_main_float_inputs(capsys):

    with patch("builtins.input", side_effect=["3.5", "1.5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: 5" in captured.out


def test_main_float_division_result(capsys):

    with patch("builtins.input", side_effect=["10", "3", "/"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result:" in captured.out


def test_main_negative_inputs(capsys):

    with patch("builtins.input", side_effect=["-10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: -5" in captured.out


# ─── main() invalid input handling ────────────────────────


def test_main_invalid_first_number(capsys):

    with patch("builtins.input", side_effect=["abc", "10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out

    assert "Result: 15" in captured.out


def test_main_invalid_second_number(capsys):

    with patch("builtins.input", side_effect=["10", "abc", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out

    assert "Result: 15" in captured.out


def test_main_space_input_rejected(capsys):

    with patch("builtins.input", side_effect=[" ", "10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out


def test_main_special_chars_rejected(capsys):

    with patch("builtins.input", side_effect=["@#$", "10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out


def test_main_empty_string_rejected(capsys):

    with patch("builtins.input", side_effect=["", "10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out


def test_main_string_with_spaces_rejected(capsys):

    with patch("builtins.input", side_effect=["12 34", "10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out


def test_main_multiple_invalid_inputs(capsys):

    with patch("builtins.input", side_effect=["abc", "xyz", "10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert captured.out.count("Invalid input") == 2


def test_main_invalid_operation(capsys):

    with patch("builtins.input", side_effect=["10", "5", "x", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid operation" in captured.out

    assert "Result: 15" in captured.out


def test_main_divide_by_zero(capsys):

    with patch("builtins.input", side_effect=["10", "0", "/"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Error: Division by zero" in captured.out
