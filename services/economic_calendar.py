import logging

from services.economic_filters import (
    is_xau_usd_relevant,
    get_impact
)


logger = logging.getLogger(__name__)


# =========================================================
# CREATE EVENT
# =========================================================

def create_event(
    title,
    event_time,
    country="US",
    forecast="-",
    previous="-",
    actual="-",
    source_name="",
    source_url=""
):

    if not is_xau_usd_relevant(
        title
    ):
        return None


    impact = get_impact(
        title
    )


    return EconomicEvent(

        title=title,

        event_time=event_time,

        impact=impact,

        country=country,

        forecast=forecast,

        previous=previous,

        actual=actual,

        source_name=source_name,

        source_url=source_url

    )


# =========================================================
# FILTER EVENTS
# =========================================================

def filter_events(
    events
):

    results = []


    for event in events:

        if not event:

            continue


        if event.country != "US":

            continue


        if not is_xau_usd_relevant(
            event.title
        ):

            continue


        if event.impact != "HIGH":

            continue


        results.append(
            event
        )


    # =========================================
    # SORT BY EVENT TIME
    # =========================================

    results.sort(
        key=lambda x: x.event_time
    )


    return results


# =========================================================
# CALENDAR
# =========================================================

def get_economic_calendar():

    """
    Mengembalikan daftar EconomicEvent.

    Untuk sekarang sumber API belum dimasukkan.
    Fungsi ini sengaja dibuat sebagai pusat kalender
    agar scheduler nantinya hanya memanggil satu fungsi.
    """

    events = []


    # =====================================================
    # SUMBER API AKAN DITAMBAHKAN DI SINI
    # =====================================================

    # BLS
    # events.extend(
    #     get_bls_events()
    # )


    # BEA
    # events.extend(
    #     get_bea_events()
    # )


    # FRED
    # events.extend(
    #     get_fred_events()
    # )


    # FEDERAL RESERVE
    # events.extend(
    #     get_fed_events()
    # )


    # ALPHA VANTAGE
    # events.extend(
    #     get_alpha_events()
    # )


    return filter_events(
        events
    )
