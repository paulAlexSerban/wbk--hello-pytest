from src.utils.math_utils import MathUtils

class TestMathUtils:
    """Unit tests for MathUtils."""

    def test_add(self):
        assert MathUtils.add(2, 3) == 5
        assert MathUtils.add(-1, 1) == 0

    def test_subtract(self):
        assert MathUtils.subtract(5, 3) == 2
        assert MathUtils.subtract(0, 0) == 0

    def test_multiply(self):
        assert MathUtils.multiply(2, 3) == 6
        assert MathUtils.multiply(-1, 1) == -1

    def test_divide(self):
        assert MathUtils.divide(6, 3) == 2
        try:
            MathUtils.divide(1, 0)
        except ValueError:
            assert True
        else:
            assert False
            
    # def test_divide_fails(self):
    #     assert MathUtils.divide(9,5) == 1.5, "failed test intentionally"