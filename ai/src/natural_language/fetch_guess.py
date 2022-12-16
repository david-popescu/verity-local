from src.guess import *
from src.guess_generator import *
from src.process_input import *
from src.natural_language import match_response


def get(user_input: str, intents) -> str:
    try:
        return select_action(user_input)

    except Exception as e:
        e.__init__()
        try:
            possible_guesses: [Guess] = []
            activations: [float] = []

            for intent in intents:
                guess_generator = GuessGenerator(intent,
                                                 user_input,
                                                 possible_guesses,
                                                 activations)

                match_response.get(guess_generator)

            return possible_guesses[activations.index(max(activations))].response

        except Exception as e:
            e.__init__()
            return 'I am sorry, sir. What do you mean?'
