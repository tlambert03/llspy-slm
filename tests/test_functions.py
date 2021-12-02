import slmgen
import pytest


@pytest.mark.parametrize("func", slmgen.__all__)
def test_functions(func):
    getattr(slmgen, func)()
