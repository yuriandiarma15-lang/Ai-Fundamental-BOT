from services.gold_price import (
    get_gold_price
)


def calculate_price_area():

    price = get_gold_price()

    # =====================================================
    # AREA AWAL
    #
    # Nanti dapat dikembangkan menggunakan:
    # ATR
    # support/resistance
    # swing
    # liquidity
    # volatility
    # =====================================================

    distance = 5.0

    buy_low = price - distance
    buy_high = price - 1.0

    sell_low = price + 1.0
    sell_high = price + distance

    support = price - distance
    resistance = price + distance

    return {

        "current_price":
            round(price, 2),

        "buy_area": (

            round(
                buy_low,
                2
            ),

            round(
                buy_high,
                2
            )

        ),

        "sell_area": (

            round(
                sell_low,
                2
            ),

            round(
                sell_high,
                2
            )

        ),

        "support":
            round(
                support,
                2
            ),

        "resistance":
            round(
                resistance,
                2
            )

    }
