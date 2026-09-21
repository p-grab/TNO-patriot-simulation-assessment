import pytest

from firing_unit import FiringUnit


def test_fire_below_probability_of_kill(monkeypatch):
    firing_unit = FiringUnit(probability_of_kill=0.8)

    monkeypatch.setattr("firing_unit.random.random", lambda: 0.5)

    assert firing_unit.fire() is True


def test_fire_equal_probability_of_kill(monkeypatch):
    firing_unit = FiringUnit(probability_of_kill=0.8)

    monkeypatch.setattr("firing_unit.random.random", lambda: 0.8)

    assert firing_unit.fire() is True


def test_fire_above_probability_of_kill(monkeypatch):
    firing_unit = FiringUnit(probability_of_kill=0.8)

    monkeypatch.setattr("firing_unit.random.random", lambda: 0.81)

    assert firing_unit.fire() is False
    
@pytest.mark.parametrize("probability", [-0.1, 1.1])
def test_invalid_probability_of_kill_raises_error(probability):
    with pytest.raises(ValueError):
        FiringUnit(probability_of_kill=probability)