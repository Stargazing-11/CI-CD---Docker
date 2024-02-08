import pytest
from fizbuz import fizzbuzz

def test_fizzbuzz_divisible_by_3_and_5(capsys):
    fizzbuzz(15)
    captured = capsys.readouterr()
    assert captured.out.strip() == "FizzBuzz"

def test_fizzbuzz_divisible_by_3(capsys):
    fizzbuzz(9)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fizz"

def test_fizzbuzz_divisible_by_5(capsys):
    fizzbuzz(10)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Buzz"

def test_fizzbuzz_not_divisible_by_3_or_5(capsys):
    fizzbuzz(7)
    captured = capsys.readouterr()
    assert captured.out.strip() == "7"

def test_fizzbuzz_zero(capsys):
    fizzbuzz(0)
    captured = capsys.readouterr()
    assert captured.out.strip() == "FizzBuzz"
