from src.string_similarity import string_similarity
from src.external.weather import get_weather
from src.external.wikipedia import search

ACTION_ARRAY: [str] = ["open", "search", "activity summary", "weather"]
ACTION_IDX: int = 0
ACTION_SCORE: float = 0.0


def reset_action() -> None:
    global ACTION_IDX
    global ACTION_SCORE

    ACTION_IDX = 0
    ACTION_SCORE = 0.0


def select_action(user_input: str, *args):
    global ACTION_ARRAY
    global ACTION_IDX
    global ACTION_SCORE

    for idx, action in enumerate(ACTION_ARRAY):
        if string_similarity(user_input.lower(), action) > ACTION_SCORE:
            ACTION_SCORE = string_similarity(user_input.lower(), action)
            ACTION_IDX = idx

    # TODO: Expand on multiple actions and response possibilities.
    if ACTION_SCORE > 0.5:
        if ACTION_ARRAY[ACTION_IDX] == 'weather':
            recommendation: str = ' I recommend wearing your scarf.'

            res = get_weather().json()
            return 'There are ' + str(res['current_weather']['temperature']) + ' degrees celsius.' + recommendation

        elif ACTION_ARRAY[ACTION_IDX] == 'search':
            return ACTION_ARRAY[ACTION_IDX] + ": " + search(args[0])
    else:
        raise
