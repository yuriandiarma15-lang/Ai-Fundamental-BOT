from services.news_sources import (
    get_all_news
)


# =========================================================
# COLLECT
# =========================================================

def collect_official_news():

    return get_all_news(
        limit_per_category=10
    )


# =========================================================
# HIGH IMPACT
# =========================================================

HIGH_IMPACT_KEYWORDS = [

    # FED

    "fomc",

    "federal reserve interest rate",

    "fed interest rate",

    "interest rate decision",

    "federal funds rate",

    "rate decision",

    "monetary policy",

    "powell speech",

    "jerome powell",


    # CPI

    "consumer price index",

    "us cpi",

    "core cpi",


    # PCE

    "personal consumption expenditures",

    "pce inflation",

    "core pce",


    # NFP

    "nonfarm payroll",

    "non-farm payroll",

    "nfp",


    # EMPLOYMENT

    "unemployment rate",

    "employment report",

    "initial jobless claims",


    # GDP

    "us gdp",

    "gross domestic product",


    # RETAIL

    "us retail sales",


    # ISM

    "ism manufacturing",

    "ism services"

]


# =========================================================
# MEDIUM
# =========================================================

MEDIUM_IMPACT_KEYWORDS = [

    "producer price index",

    "ppi",

    "industrial production",

    "capacity utilization",

    "durable goods",

    "consumer confidence",

    "michigan sentiment",

]


# =========================================================
# EXCLUDE
# =========================================================

EXCLUDE_KEYWORDS = [

    "football",

    "soccer",

    "basketball",

    "tennis",

    "celebrity",

    "movie",

    "music",

    "fashion",

    "recipe",

    "casino",

    "sports betting",

]


# =========================================================
# CLASSIFY
# =========================================================

def classify_news(
    title,
    description=""
):

    text = (

        f"{title} "
        f"{description}"

    ).lower()


    # =====================================================
    # EXCLUDE
    # =====================================================

    for keyword in EXCLUDE_KEYWORDS:

        if keyword in text:

            return None


    # =====================================================
    # HIGH
    # =====================================================

    for keyword in HIGH_IMPACT_KEYWORDS:

        if keyword in text:

            return "HIGH"


    # =====================================================
    # MEDIUM
    # =====================================================

    for keyword in MEDIUM_IMPACT_KEYWORDS:

        if keyword in text:

            return "MEDIUM"


    return "LOW"


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


        impact = classify_news(

            title,

            description

        )


        if impact != "HIGH":

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
        f"🔥 HIGH IMPACT: "
        f"{len(results)}"
    )


    return results
