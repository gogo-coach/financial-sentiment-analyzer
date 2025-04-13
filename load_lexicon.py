import json

def load_custom_lexicon(filepath="custom_lexicon.json"):
    with open(filepath, "r", encoding="utf-8") as f:
        custom_lex = json.load(f)
    return custom_lex
