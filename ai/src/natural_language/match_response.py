from src.guess_generator import *
from src.string_similarity import *
from src.natural_language.set_activation import *


def get(guess_generator: GuessGenerator) -> None:
    for pattern in guess_generator.intent['patterns']:
        current_activation: float = string_similarity(
            guess_generator.user_input.lower(), pattern)

        set_activation(current_activation, guess_generator)
