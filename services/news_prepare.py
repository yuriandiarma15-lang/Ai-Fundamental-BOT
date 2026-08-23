from datetime import timedelta

from services.price_area import (
    calculate_price_area
)

from services.fundamental_analyzer import (
    analyze_text
)

from services.signal_formatter import (
    format_prepare
)


def prepare_news(
    event
):

    fundamental = analyze_text(
        event.title
    )

    area = calculate_price_area()

    return format_prepare(
        event,
        area,
        fundamental
    )
