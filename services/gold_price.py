import requests

from config.settings import (
    TWELVE_DATA_API_KEY
)


def get_gold_price():

    if not TWELVE_DATA_API_KEY:

        raise RuntimeError(
            "TWELVE_DATA_API_KEY belum diisi."
        )

    url = (
        "https://api.twelvedata.com/price"
    )

    params = {

        "symbol": "XAU/USD",

        "apikey":
            TWELVE_DATA_API_KEY

    }

    response = requests.get(
        url,
        params=params,
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    if "price" not in data:

        raise RuntimeError(
            f"Gold price error: {data}"
        )

    return float(
        data["price"]
    )
