import pytest


@pytest.mark.parametrize("x", [2, 4, 6, 8, 10])
class TestNumbers:
    def test_positive(self, x):
        assert x > 0

    def test_even(self, x):
        assert x % 2 == 0
