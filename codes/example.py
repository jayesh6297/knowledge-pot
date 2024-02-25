from dataclasses import dataclasses

@dataclasses
class User:
    id: str
    name: str
    age: float
    weight: float
    addr: []str