from dataclasses import dataclasses
from typing import List

@dataclasses
class User:
    id: str
    name: str
    age: float
    weight: float
    addr: List[str]
