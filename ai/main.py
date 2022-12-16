import json
from src.natural_language import fetch_guess

INTENTS_FILE = open(
    '/Users/davidpopescu/Desktop/tmp/project-v/verity/ai/intents.json')
INTENTS = json.load(INTENTS_FILE)
INTENTS_FILE.close()

USER_INPUT_FILE = open(
    '/Users/davidpopescu/Desktop/tmp/project-v/verity/user-input.json')
USER_INPUT = json.load(USER_INPUT_FILE)
USER_INPUT_FILE.close()

OUTPUT: str = "{\"response\":\"" + fetch_guess.get(USER_INPUT['user_input'], INTENTS) + "\"}"

RESPONSE_FILE = open(
    "/Users/davidpopescu/Desktop/tmp/project-v/verity/response.json", "w")
RESPONSE_FILE.write(OUTPUT)
RESPONSE_FILE.close()

# reset_action()
# print(fetch_guess('weather'))
# reset_action()
