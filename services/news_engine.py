from services.news_sources import (
    get_official_news
)


def collect_official_news():

    sources = [
        "FED",
        "TREASURY",
        "BLS"
    ]

    all_news = []

    for source in sources:

        news = get_official_news(
            source
        )

        all_news.extend(
            news
        )

    return all_news


def find_high_impact_news(
    news_list
):

    keywords = [

        "fomc",
        "federal reserve",
        "interest rate",
        "cpi",
        "consumer price index",
        "nonfarm payroll",
        "employment",
        "unemployment",
        "pce",
        "powell"

    ]

    results = []

    for news in news_list:

        title = (
            news.get(
                "title",
                ""
            )
            .lower()
        )

        for keyword in keywords:

            if keyword in title:

                news["impact"] = "HIGH"

                results.append(
                    news
                )

                break

    return results
