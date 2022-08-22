from typing import Any
from dataclasses import dataclass


@dataclass()
class Node:

    count: int
    weight: int
    total_weight: int
    previous: Any = None

    def __post_init__(self):
        self.total_weight += self.count * self.weight
