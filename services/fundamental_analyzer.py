import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


RULE_FILE = os.path.join(
    BASE_DIR,
    "data",
    "fundamental_rules.json"
)


def load_rules():

    try:

        with open(
            RULE_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return {
            "bullish_gold": [],
            "bearish_gold": []
        }


RULES = load_rules()


def analyze_text(
    text: str
):

    text = (
        text
        .lower()
        .strip()
    )

    bullish_score = 0
    bearish_score = 0

    bullish_matches = []
    bearish_matches = []

    for phrase in RULES.get(
        "bullish_gold",
        []
    ):

        if phrase in text:

            bullish_score += 1

            bullish_matches.append(
                phrase
            )

    for phrase in RULES.get(
        "bearish_gold",
        []
    ):

        if phrase in text:

            bearish_score += 1

            bearish_matches.append(
                phrase
            )

    total = (
        bullish_score
        + bearish_score
    )

    if total == 0:

        return {

            "bias": "NEUTRAL",

            "score": 50,

            "bullish_matches": [],

            "bearish_matches": []

        }

    if bullish_score > bearish_score:

        score = min(
            50 + bullish_score * 10,
            95
        )

        bias = "BULLISH"

    elif bearish_score > bullish_score:

        score = min(
            50 + bearish_score * 10,
            95
        )

        bias = "BEARISH"

    else:

        score = 50

        bias = "NEUTRAL"

    return {

        "bias": bias,

        "score": score,

        "bullish_matches":
            bullish_matches,

        "bearish_matches":
            bearish_matches

    }
