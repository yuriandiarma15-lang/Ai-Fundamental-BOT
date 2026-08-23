from services.price_area import (
    calculate_price_area
)

from services.fundamental_analyzer import (
    analyze_text
)

from services.signal_formatter import (
    format_prepare
)


# =========================================================
# PREPARE HIGH IMPACT NEWS
# =========================================================

def prepare_news(
    event
):

    # =====================================================
    # ANALISIS FUNDAMENTAL
    # =====================================================

    text = (

        f"{event.title} "

        f"Actual {getattr(event, 'actual', '-')} "

        f"Forecast {getattr(event, 'forecast', '-')} "

        f"Previous {getattr(event, 'previous', '-')}"
    )


    fundamental = analyze_text(
        text
    )


    # =====================================================
    # HITUNG AREA HARGA XAUUSD
    # =====================================================

    area = calculate_price_area()


    # =====================================================
    # FORMAT TELEGRAM
    # =====================================================

    return format_prepare(
        event,
        area,
        fundamental
    )
