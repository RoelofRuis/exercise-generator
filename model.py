from __future__ import annotations

import random
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


class ConstraintOption(NamedTuple):
    placeholder: str
    choices: List[str]


class Constraint(NamedTuple):
    stencil: str
    options: List[ConstraintOption] = []

    @property
    def description(self) -> str:
        descr = self.stencil
        for opt in self.options:
            selected = random.choice(opt.choices)
            descr = descr.replace(opt.placeholder, selected)
        return descr


class ExerciseOptions(NamedTuple):
    outputs: List[Output]
    forms: List[Form]
    tempo: Constraint
    metre: Constraint
    key: List[Constraint]
    emotion: Constraint
    place: Constraint
    atmosphere: Constraint
    general: List[Constraint]


class Selection(NamedTuple):
    min: int
    max: int
