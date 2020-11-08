from __future__ import annotations

from typing import NamedTuple, List


class DurationModifier(NamedTuple):
    a: float = 0.0
    b: float = 0.0
    x: float = 0.0

    @property
    def value(self) -> float:
        return (self.a * self.x) + self.b

    def add(self, that: DurationModifier) -> DurationModifier:
        return DurationModifier(self.a + that.a, self.b + that.b, self.x + that.x)


class Output(NamedTuple):
    description: str
    duration_mod: DurationModifier


class Form(NamedTuple):
    name: str
    num_bar_options: List[int]


class Atmosphere(NamedTuple):
    name: str


class ConstraintOption(NamedTuple):
    placeholder: str
    choices: List[str]


class Constraint(NamedTuple):
    description: str
    options: List[ConstraintOption] = []


class ExerciseOptions(NamedTuple):
    outputs: List[Output]
    forms: List[Form]
    tempi: List[Constraint]
    atmospheres: List[Atmosphere]
    general: List[Constraint]


class Selection(NamedTuple):
    min: int
    max: int
