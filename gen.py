from model import *


def generate_exercise(option: ExerciseOptions, num_atmospheres: Selection, num_general_constraints: Selection) -> str:
    output = random.choice(option.outputs)
    form = random.choice(option.forms)
    num_bars = random.choice(form.num_bar_options)
    tempo = random.choice(option.tempi)
    atmospheres = random.sample(option.atmospheres, random.randint(num_atmospheres.min, num_atmospheres.max))
    constraints = random.sample(option.general, random.randint(num_general_constraints.min, num_general_constraints.max))

    atmosphere_descr = ' '.join([a.name for a in atmospheres])
    if len(constraints) > 0:
        joined_constraints = '\nen '.join([c.description for c in constraints])
        constraint_descr = f'\nBeperk je door {joined_constraints}'
    else:
        constraint_descr = ''

    duration = output.duration_mod.add(DurationModifier(x=num_bars)).value

    return f'Schrijf {output.description} voor een {atmosphere_descr} {form.name} van {num_bars} maten in {tempo.description}' \
           f'{constraint_descr}' \
           f'\nGebruik hiervoor {duration} minuten'


OPTIONS = ExerciseOptions(
    outputs=[
        Output(description='melodie', duration_mod=DurationModifier(1.0)),
        Output(description='melodie en harmonie', duration_mod=DurationModifier(2.5))
    ],
    forms=[
        Form(name='het motief', num_bar_options=[2, 4, 6, 8]),
        Form(name='het thema', num_bar_options=[4, 8])
    ],
    tempi=[
        Constraint('{tempo} tempo', [
            ConstraintOption('{tempo}', ['langzaam', 'gemiddeld', 'snel'])
        ])
    ],
    atmospheres=[
        Atmosphere('agitated'),
        Atmosphere('dark'),
        Atmosphere('light'),
        Atmosphere('uplifting'),
        Atmosphere('dense'),
    ],
    general=[
        Constraint('alleen {note} noten te gebruiken', [
            ConstraintOption('{note}', ['kwart', 'achtste'])
        ]),
        Constraint('geen noten op de zware maatdelen te plaatsen'),
    ]
)


exercise = generate_exercise(OPTIONS, Selection(1, 1), Selection(0, 2))
print(exercise)
