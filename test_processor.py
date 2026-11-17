"""Hypothesis fuzz tests for all three processor functions."""

from hypothesis import given, strategies as st

from processor import calculate_average, is_palindrome, parse_int_list


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_parse_int_list_never_crashes(value):
    parse_int_list(value)


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_is_palindrome_never_crashes(value):
    is_palindrome(value)


@given(st.lists(st.one_of(st.integers(), st.text(), st.none())))
def test_calculate_average_never_crashes(values):
    calculate_average(values)


def test_expected_normal_cases():
    assert parse_int_list("10, 20,30") == [10, 20, 30]
    assert is_palindrome("Never odd or even") is True
    assert calculate_average([10, 20, 30]) == 20
