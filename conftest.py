from typing import List, Tuple
from pathlib import Path

import pytest


RESOURCES = Path(__file__).parent / "test" / "resources"

@pytest.fixture
def correct_sums() -> List[Tuple[int, int, int]]:

    sums = list()
    with (RESOURCES / "sums.txt").open() as f:
        for line in f:
            sums.append(tuple(int(i) for i in line.split(" ")))

    return sums