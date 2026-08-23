import time

from services.news_sources import (
    get_all_news
)

from services.news_engine import (
    find_high_impact_news
)

from config.settings import (
    NEWS_REFRESH_SECONDS
)


_cached_news = []

_cached_high_impact = []

_last_update = 0


# =========================================================
# REFRESH
# =========================================================

def refresh_news(
    force=False
):

    global _cached_news
    global _cached_high_impact
    global _last_update


    now = time.time()


    # =====================================================
    # CACHE MASIH VALID
    # =====================================================

    if (

        not force

        and _cached_news

        and now - _last_update
        < NEWS_REFRESH_SECONDS

    ):

        print(
            "🟢 NEWS CACHE MASIH VALID"
        )

        return (
            _cached_news,
            _cached_high_impact
        )


    # =====================================================
    # UPDATE
    # =====================================================

    print(
        "🔄 REFRESH GNEWS..."
    )


    news = get_all_news(
        limit_per_category=10
    )


    high_impact = (
        find_high_impact_news(
            news
        )
    )


    _cached_news = news

    _cached_high_impact = high_impact

    _last_update = now


    print(
        f"✅ NEWS CACHE UPDATED: "
        f"{len(news)}"
    )


    print(
        f"🔥 HIGH IMPACT CACHE: "
        f"{len(high_impact)}"
    )


    return (
        _cached_news,
        _cached_high_impact
    )


# =========================================================
# GET CACHE
# =========================================================

def get_cached_news():

    return (
        _cached_news,
        _cached_high_impact
    )
