from typing import NamedTuple, List


class Output(NamedTuple):
    value: str
    per_bar_dur: float


class Form(NamedTuple):
    name: str
    num_bar_options: List[int]
    duration_multiplier: float = 1.0


class Tempo(NamedTuple):
    name: str


class Atmosphere(NamedTuple):
    name: str


class Constraint(NamedTuple):
    description: str


class IdeaOptions(NamedTuple):
    outputs: List[Output]
    forms: List[Form]
    tempi: List[Tempo]
    atmospheres: List[Atmosphere]
    constraints: List[Constraint]


OPTIONS = IdeaOptions(
    outputs=[
        Output(value="melody", per_bar_dur=1.0),
        Output(value="melody and harmony", per_bar_dur=2.5)
    ],
    forms=[
        Form(name="motive", num_bar_options=[2, 4, 6, 8]),
        Form(name="theme", num_bar_options=[4, 8])
    ],
    tempi=[
        Tempo("slow"), Tempo("medium"), Tempo("quick")
    ],
    atmospheres=[
        Atmosphere("agitated"),
        Atmosphere("dark"),
        Atmosphere("light"),
        Atmosphere("uplifting"),
        Atmosphere("dense"),
    ],
    constraints=[

    ]
)
