from services.news_sources import (
    get_all_news
)


# =========================================================
# COLLECT NEWS
# =========================================================

def collect_official_news():

    return get_all_news(
        limit_per_category=10
    )


# =========================================================
# HIGH IMPACT KEYWORDS
# =========================================================

HIGH_IMPACT_KEYWORDS = [

    # FED

    "fomc",
    "federal reserve",
    "fed rate",
    "interest rate",
    "rate decision",
    "monetary policy",
    "powell",
    "jerome powell",

    # INFLATION

    "cpi",
    "consumer price index",
    "inflation",
    "pce",
    "core pce",
    "ppi",
    "producer price index",

    # EMPLOYMENT

    "nfp",
    "nonfarm payroll",
    "non-farm payroll",
    "unemployment rate",
    "jobless claims",
    "employment report",

    # GDP

    "gdp",
    "gross domestic product",

    # GOLD / USD

    "gold price",
    "gold",
    "xauusd",
    "us dollar",
    "usd"

]


# =========================================================
# EXCLUDE
# =========================================================

EXCLUDE_KEYWORDS = [

    "sports",
    "football",
    "soccer",
    "basketball",
    "celebrity",
    "movie",
    "entertainment",
    "recipe",
    "fashion",
    "real estate",
    "crypto casino"

]


# =========================================================
# CHECK HIGH IMPACT
# =========================================================

def is_high_impact_news(
    title,
    description=""
):

    text = (

        f"{title} "
        f"{description}"

    ).lower().strip()


    # =====================================================
    # EXCLUDE
    # =====================================================

    for keyword in EXCLUDE_KEYWORDS:

        if keyword in text:

            return False


    # =====================================================
    # HIGH IMPACT
    # =====================================================

    for keyword in HIGH_IMPACT_KEYWORDS:

        if keyword in text:

            return True


    return False


# =========================================================
# FIND HIGH IMPACT
# =========================================================

def find_high_impact_news(
    news_list
):

    results = []

    seen = set()


    for news in news_list:

        title = news.get(
            "title",
            ""
        )


        description = news.get(
            "description",
            ""
        )


        if not is_high_impact_news(

            title,

            description

        ):

            continue


        normalized = (

            title
            .lower()
            .strip()

        )


        if normalized in seen:

            continue


        seen.add(
            normalized
        )


        news["impact"] = "HIGH"


        results.append(
            news
        )


    print(
        f"🔥 HIGH IMPACT FILTER: "
        f"{len(results)}"
    )


    return results
