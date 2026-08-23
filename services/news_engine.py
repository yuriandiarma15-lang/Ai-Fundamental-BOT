import asyncio

from services.news_sources import get_official_news


# =========================================================
# SOURCES
# =========================================================

NEWS_SOURCES = [
    "FED",
    "TREASURY",
    "BLS",
]


# =========================================================
# COLLECT NEWS
# =========================================================

async def collect_official_news_async():

    tasks = [
        asyncio.to_thread(
            get_official_news,
            source
        )
        for source in NEWS_SOURCES
    ]

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    all_news = []

    for source, result in zip(
        NEWS_SOURCES,
        results
    ):

        if isinstance(result, Exception):

            print(
                f"❌ NEWS ERROR [{source}]:",
                repr(result)
            )

            continue

        if result:

            all_news.extend(
                result
            )

    return all_news


# =========================================================
# SYNC VERSION
# =========================================================

def collect_official_news():

    all_news = []

    for source in NEWS_SOURCES:

        try:

            news = get_official_news(
                source
            )

            if news:

                all_news.extend(
                    news
                )

        except Exception as e:

            print(
                f"❌ NEWS SOURCE ERROR [{source}]:",
                repr(e)
            )

    return all_news


# =========================================================
# HIGH IMPACT KEYWORDS
# =========================================================

HIGH_IMPACT_KEYWORDS = [

    "fomc",
    "fomc meeting",
    "fomc statement",
    "fomc minutes",

    "federal funds rate",
    "interest rate decision",
    "interest rate",
    "fed rate",
    "rate decision",

    "monetary policy",

    "powell",
    "jerome powell",
    "fed chair",
    "fed chairman",

    "beige book",

    "consumer price index",
    "cpi",
    "core cpi",

    "producer price index",
    "ppi",
    "core ppi",

    "pce",
    "core pce",
    "personal consumption expenditures",

    "nonfarm payroll",
    "non-farm payroll",
    "nfp",

    "unemployment rate",
    "employment situation",
    "employment report",

    "jobless claims",
    "initial jobless claims",
    "continuing jobless claims",

    "average hourly earnings",

    "gross domestic product",
    "gdp",

    "retail sales",
    "durable goods",

    "industrial production",

    "ism manufacturing",
    "ism services",

    "pmi",

    "consumer confidence",
    "consumer sentiment",
    "michigan consumer sentiment",
]


# =========================================================
# EXCLUDE
# =========================================================

EXCLUDE_KEYWORDS = [

    "enforcement action",
    "enforcement actions",
    "former employee",

    "bank application",
    "application by",
    "approval of application",
    "approves application",

    "bank holding company",
    "acquisition",
    "merger",
    "branch",

    "consent order",
    "cease and desist",
    "civil money penalty",
    "regulatory action",

    "banking organization",
    "financial institution",

    "deutsche bank",
    "national westminster",
    "bancshares",
]


# =========================================================
# CHECK
# =========================================================

def is_high_impact_news(title):

    if not title:

        return False

    text = (
        title
        .lower()
        .strip()
    )

    for keyword in EXCLUDE_KEYWORDS:

        if keyword in text:

            return False

    for keyword in HIGH_IMPACT_KEYWORDS:

        if keyword in text:

            return True

    return False


# =========================================================
# FIND
# =========================================================

def find_high_impact_news(news_list):

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
