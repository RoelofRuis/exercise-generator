from typing import NamedTuple, List


class Output(NamedTuple):
    description: str
    per_bar_dur: float


class Form(NamedTuple):
    name: str
    num_bar_options: List[int]
    duration_multiplier: float = 1.0


class Tempo(NamedTuple):
    name: str


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
    tempi: List[Tempo]
    atmospheres: List[Atmosphere]
    general: List[Constraint]


class Selection(NamedTuple):
    min: int
    max: int
