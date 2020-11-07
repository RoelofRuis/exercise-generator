import random

from model import *


def random_pick(lst: list):
    index = random.randint(0, len(lst) - 1)
    return lst[index]


def generate_idea(option: IdeaOptions) -> str:
    # Pick 1 output (expand to multiple instruments later on?)
    # Pick one form, from it, pick number of bars
    # Pick one tempo
    # Pick n atmospheres
    # Pick m constraints
    pass


idea = generate_idea(OPTIONS)
print(idea)

# print(f"Write the {output} for a {bars} bar {atmosphere} {form} in {tempo} tempo\n")
