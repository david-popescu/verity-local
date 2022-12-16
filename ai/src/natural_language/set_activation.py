import random
from src.guess import *


def set_activation(current_activation, guess_generator) -> None:
    if current_activation > 0.5:
        guess = Guess(current_activation,
                      random.choice(guess_generator.intent['responses']),
                      guess_generator.intent['context'])

        guess_generator.activations.append(current_activation)
        guess_generator.possible_guesses.append(guess)
