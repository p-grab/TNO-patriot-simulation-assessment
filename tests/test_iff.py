import pytest

from iff import IFF


def test_iff_more_odd_than_even():
    iff = IFF()
    sequence = ["0000001", "0000011", "0000010"]

    assert iff.is_hostile_entity_detected(sequence) is True


def test_iff_more_even_than_odd():
    iff = IFF()
    sequence = ["0000000", "0000010", "0000001"]

    assert iff.is_hostile_entity_detected(sequence) is False


def test_iff_equal_odd_and_even():
    iff = IFF()
    sequence = ["0000001", "0000010"]

    assert iff.is_hostile_entity_detected(sequence) is False


def test_iff_invalid_binary_letters():
    iff = IFF()

    with pytest.raises(ValueError):
        iff.is_hostile_entity_detected(["abcdefg"])


def test_iff_invalid_binary_letter_with_numbers():
    iff = IFF()

    with pytest.raises(ValueError):
        iff.is_hostile_entity_detected(["010a101"])


def test_iff_empty_sequence():
    iff = IFF()

    assert iff.is_hostile_entity_detected([]) is False