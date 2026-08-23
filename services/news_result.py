from services.price_area import (
    calculate_price_area
)

from services.fundamental_analyzer import (
    analyze_text
)

from services.signal_formatter import (
    format_result
)


def process_news_result(
    event
):

    text = (

        f"{event.title} "

        f"Actual {event.actual} "

        f"Forecast {event.forecast} "

        f"Previous {event.previous}"

    )

    fundamental = analyze_text(
        text
    )

    area = calculate_price_area()

    return format_result(
        event,
        area,
        fundamental
    )
