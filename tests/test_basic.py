import subprocess
import sys
from pathlib import Path

import pytest

from examples.basic_usage import Person, main


def invoke(file: Path, *args):
    cmd = [sys.executable, str(file), *args]
    return subprocess.check_output(cmd).decode("utf-8")


@pytest.fixture
def basic(example_root) -> Path:
    yield example_root / "basic_usage.py"


def test_cli(basic):
    out = invoke(basic, "--help")
    assert Person.__doc__ in out
    for field, info in Person.model_fields.items():
        assert field in out
        assert info.description in out
    print(out)
