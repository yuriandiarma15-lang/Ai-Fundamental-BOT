import feedparser
from urllib.parse import quote


BASE_URL = "https://news.google.com/rss/search?q="


SEARCHES = {
    "XAUUSD": "gold price OR XAUUSD",
    "FED": "Federal Reserve OR FOMC OR Powell",
    "USD": "US dollar OR USD",
    "CPI": "US CPI OR inflation",
    "NFP": "NFP OR nonfarm payrolls",
    "PCE": "US PCE inflation",
}


def get_news(
    category: str,
    limit: int = 10
):

    query = SEARCHES.get(
        category
    )

    if not query:
        return []

    url = (
        BASE_URL
        + quote(query)
        + "&hl=en-US"
        + "&gl=US"
        + "&ceid=US:en"
    )

    try:

        feed = feedparser.parse(
            url
        )

        results = []

        for item in feed.entries[:limit]:

            results.append({

                "category":
                    category,

                "title":
                    item.get(
                        "title",
                        ""
                    ),

                "link":
                    item.get(
                        "link",
                        ""
                    ),

                "published":
                    item.get(
                        "published",
                        ""
                    ),

                "source":
                    item.get(
                        "source",
                        {}
                    ).get(
                        "title",
                        "Google News"
                    )

            })

        return results

    except Exception as e:

        print(
            "GOOGLE NEWS ERROR:",
            repr(e)
        )

        return []
