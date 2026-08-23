import feedparser


# =========================================================
# OFFICIAL SOURCES
# =========================================================

OFFICIAL_SOURCES = {

    "FED":

        "https://www.federalreserve.gov/feeds/press_all.xml",

    "TREASURY":

        "https://home.treasury.gov/rss/press-releases.xml",

    "BLS":

        "https://www.bls.gov/feed/bls_latest.rss",

}


# =========================================================
# GET RSS NEWS
# =========================================================

def get_official_news(
    source_name: str,
    limit: int = 10
):

    url = OFFICIAL_SOURCES.get(
        source_name
    )

    if not url:
        return []

    try:

        feed = feedparser.parse(
            url
        )

        results = []

        for item in feed.entries[:limit]:

            results.append({

                "source": source_name,

                "title": item.get(
                    "title",
                    ""
                ),

                "link": item.get(
                    "link",
                    ""
                ),

                "published": item.get(
                    "published",
                    ""
                )

            })

        return results

    except Exception:

        return []
