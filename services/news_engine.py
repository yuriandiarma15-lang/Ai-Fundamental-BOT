from services.news_sources import get_news


CATEGORIES = [
    "XAUUSD",
    "FED",
    "USD",
    "CPI",
    "NFP",
    "PCE",
]


INCLUDE_KEYWORDS = [

    "gold",
    "xauusd",
    "xau",

    "federal reserve",
    "fomc",
    "powell",

    "interest rate",
    "fed rate",
    "rate decision",

    "cpi",
    "inflation",
    "pce",

    "nonfarm payroll",
    "non-farm payroll",
    "nfp",

    "unemployment",
    "jobless claims",

    "us dollar",
    "usd",
    "dollar",

    "treasury yield",
    "bond yield",

]


EXCLUDE_KEYWORDS = [

    "bank application",
    "application by",
    "enforcement action",
    "former employee",
    "merger",
    "acquisition",
    "bancshares",
    "branch",
    "consent order",
    "civil money penalty",

]


def collect_official_news():

    all_news = []

    for category in CATEGORIES:

        try:

            news = get_news(
                category,
                limit=10
            )

            all_news.extend(
                news
            )

        except Exception as e:

            print(
                f"NEWS ERROR [{category}]:",
                repr(e)
            )

    return all_news


def is_high_impact_news(
    title
):

    if not title:

        return False

    text = (
        title
        .lower()
        .strip()
    )

    # Buang berita tidak relevan
    for keyword in EXCLUDE_KEYWORDS:

        if keyword in text:

            return False

    # Cari berita relevan
    for keyword in INCLUDE_KEYWORDS:

        if keyword in text:

            return True

    return False


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

        if not is_high_impact_news(
            title
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

    return results
