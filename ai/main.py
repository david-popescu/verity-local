import json
import random
from src.guess import Guess
from src.guess_generator import GuessGenerator
from src.string_similarity import string_similarity
from src.process_input import select_action, reset_action

INTENTS_FILE = open(
    '/Users/davidpopescu/Desktop/tmp/project-v/verity/ai/intents.json')
INTENTS = json.load(INTENTS_FILE)
INTENTS_FILE.close()


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
    try:
        possible_guesses: [Guess] = []
        activations: [float] = []

        for intent in INTENTS:
            guess_generator = GuessGenerator(intent,
                                             user_input,
                                             possible_guesses,
                                             activations)

            generate_best_response(guess_generator)

        return possible_guesses[activations.index(max(activations))].response

    except Exception as e:
        e.__init__()
        return 'I am sorry, sir. What do you mean?'


# reset_action()
# print(fetch_guess('weather'))
# reset_action()

USER_INPUT_FILE = open(
    '/Users/davidpopescu/Desktop/tmp/project-v/verity/user-input.json')
USER_INPUT = json.load(USER_INPUT_FILE)
USER_INPUT_FILE.close()

OUTPUT: str = "{\"response\":\"" + fetch_guess(USER_INPUT['user_input']) + "\"}"

RESPONSE_FILE = open(
    "/Users/davidpopescu/Desktop/tmp/project-v/verity/response.json", "w")
RESPONSE_FILE.write(OUTPUT)
RESPONSE_FILE.close()

# IO_FILE = open(
# "/Users/davidpopescu/Desktop/tmp/project-v/verity/IO.json", "w")
# IO_FILE.write(select_action("weather"))
# reset_action()
# IO_FILE.write(select_action("search", "Dog"))
# reset_action()
# IO_FILE.write(fetch_guess("Hello!"))
# IO_FILE.close()

# print(select_action("weather"))
# reset_action()
# print(select_action("search", "Dog"))
# reset_action()
#
# print(fetch_guess("Hello!"))
