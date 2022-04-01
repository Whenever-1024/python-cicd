from __future__ import print_function
import random

character = (
    "Hero", 
    "Recruit",
    "Invader",
    "Commander",
    "Children",
    "Spies",
    "Commanders",
    "Soldier",
    "Droids",
    "Veterans",
    "Beasts",
    "Chase",
    "Construction",
    "Honor",
    "Confinement",
    "Defenseless",
    "Alerted",
    "Light",
    "Afraid",
    "Failing",
    "Courage",
    "Demand",
    "Life"
)

final_phrase = (
    "Men's Legacy",
    "The Flight",
    "Tentacles",
    "Men's Legacy",
    "New Worlds",
    "The Future",
    "Four Eyes",
    "Everywhere",
    "Guests",
    "Robots",
    "Directors",
    "Armies",
    "Outer Space",
    "Honor",
    "The Droids",
    "The New World",
    "The Void Of Space",
    "Time Travel",
    "Orbit",
    "The Mists",
    "The New World",
    "New Earth",
    "My Journey",
    "The Machines"
)

connectors = (
    "Of", 
    "In",
    "With",
    "And",
    "By",
    "For",
    "Against"
)


def sample(the_sample= None, n = 1):
    result = random.sample(the_sample, n)
    if n == 1:
        return result[0]
    return result


def generate_movie():
    phrase = ' '.join([sample(character), sample(connectors), sample(final_phrase)])
    return phrase.title()


if __name__ == "__main__":
    print(generate_movie())
