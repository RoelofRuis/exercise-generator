from model import *


def generate_exercise(option: ExerciseOptions, num_general_constraints: Selection) -> str:
    output = random.choice(option.outputs)
    form = random.choice(option.forms)
    num_bars = random.choice(form.num_bar_options)
    constraints = random.sample(option.general, random.randint(num_general_constraints.min, num_general_constraints.max))

    key = random.choice(option.key)

    if len(constraints) > 0:
        joined_constraints = '\nen '.join([c.description for c in constraints])
        constraint_descr = f'\nBeperk je door {joined_constraints}'
    else:
        constraint_descr = ''

    duration = output.duration_mod.add(DurationModifier(x=num_bars)).value

    return f'Schrijf {output.description} voor een {form.name} van {num_bars} maten' \
           f'\nTempo:     {option.tempo.description}' \
           f'\nToonsoort: {key.description}' \
           f'\nMaatsoort: {option.metre.description}' \
           f'\nSfeer:     {option.atmosphere.description}' \
           f'\n{option.emotion.description} {option.place.description}' \
           f'{constraint_descr}' \
           f'\nGebruik hiervoor {duration} minuten'


OPTIONS = ExerciseOptions(
    outputs=[
        Output(description='de melodie', duration_mod=DurationModifier(1.0)),
        Output(description='de melodie en harmonie', duration_mod=DurationModifier(2.5))
    ],
    forms=[
        Form(name='een motief', num_bar_options=[2, 4, 6, 8]),
        Form(name='een thema', num_bar_options=[4, 8])
    ],
    tempo=Constraint('{tempo}', [
        ConstraintOption('{tempo}', ['langzaam', 'gemiddeld', 'snel'])
    ]),
    metre=Constraint('{metre}', [
        ConstraintOption('{metre}', ['4/4', '3/4'])
    ]),
    key=[
        Constraint('{note} majeur', [
            ConstraintOption('{note}', ['C', 'F', 'G'])
        ]),
        Constraint('{note} mineur', [
            ConstraintOption('{note}', ['A', 'E', 'D'])
        ])
    ],
    emotion=Constraint('{emotion}', [
        ConstraintOption('{emotion}', [
            'in adoratie', 'in afschuw', 'angstig', 'bang', 'bedroefd', 'in bewondering', 'geïnteresseerd', 'jaloers',
            'kalm', 'nostalgisch', 'ongemakkelijk', 'in ontzag', 'opgewonden', 'een romance', 'tevreden', 'verveeld',
            'verward'
        ])
    ]),
    place=Constraint('{place}', [
        ConstraintOption('{place}', ['bij de bakker', 'in een weiland', 'in een drukke stad', 'op een feest',
                                     'onderweg naar je schoonfamilie', 'in een winkelstraat', 'in een leeg warenhuis',
                                     'in de bossen', 'in een oude tabakszaak', 'op een brug', 'aan het water'
        ]),
    ]),
    atmosphere=Constraint('{atmosphere}', [
        ConstraintOption('{atmosphere}', ['donker', 'licht', 'flitsend', 'dicht', 'open', 'complex', 'eenvoudig'])
    ]),
    general=[
        Constraint('alleen {note} noten te gebruiken', [
            ConstraintOption('{note}', ['kwart', 'achtste'])
        ]),
        Constraint('geen noten op de zware maatdelen te plaatsen'),
    ]
)


exercise = generate_exercise(OPTIONS, Selection(0, 2))
print(exercise)
