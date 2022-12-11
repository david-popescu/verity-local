import json
import random
from src.guess import Guess
from src.guess_generator import GuessGenerator
from src.string_similarity import string_similarity
from src.process_input import select_action, reset_action

intents_file = open('intents.json')
INTENTS = json.load(intents_file)


def set_activation(current_activation, guess_generator) -> None:
    if current_activation > 0.5:
        guess = Guess(current_activation,
                      random.choice(guess_generator.intent['responses']),
                      guess_generator.intent['context'])

        guess_generator.activations.append(current_activation)
        guess_generator.possible_guesses.append(guess)


def generate_best_response(guess_generator: GuessGenerator) -> None:
    for pattern in guess_generator.intent['patterns']:
        current_activation: float = string_similarity(
            guess_generator.user_input.lower(), pattern)

        set_activation(current_activation, guess_generator)


def fetch_guess(user_input: str) -> str:
    possible_guesses: [Guess] = []
    activations: [float] = []

    for intent in INTENTS:
        guess_generator = GuessGenerator(intent,
                                         user_input,
                                         possible_guesses,
                                         activations)

        generate_best_response(guess_generator)

    return possible_guesses[activations.index(max(activations))].response


print(select_action("weather"))
reset_action()
print(select_action("search", "Dog"))
reset_action()

print(fetch_guess("Hello!"))
