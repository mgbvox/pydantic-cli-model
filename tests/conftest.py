from pathlib import Path

import pytest

@pytest.fixture
def example_root()->Path:
    return Path(__file__).parent.parent / "examples"