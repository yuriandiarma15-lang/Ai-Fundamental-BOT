import requests

from config.settings import (
    GNEWS_API_KEY
)


GNEWS_URL = (
    "https://gnews.io/api/v4/search"
)


# =========================================================
# QUERY
# =========================================================

SEARCHES = {

    "FED":
        '"Federal Reserve" OR FOMC OR Powell',

    "CPI":
        '"US CPI" OR "consumer price index"',

    "NFP":
        '"NFP" OR "nonfarm payroll"',

    "PCE":
        '"US PCE" OR "personal consumption expenditures"',

    "USD":
        '"US dollar" OR USD',

    "XAUUSD":
        '"gold price" OR XAUUSD',

}


# =========================================================
# GET SOURCE
# =========================================================

def get_source_name(article):

    source = article.get(
        "source",
        {}
    )

    if isinstance(source, dict):

        return source.get(
            "name",
            "GNews"
        )

    return "GNews"


# =========================================================
# GET NEWS
# =========================================================

def get_news(
    category: str,
    limit: int = 10
):

    print(
        f"📰 GNEWS REQUEST: {category}"
    )


    if not GNEWS_API_KEY:

        print(
            "❌ GNEWS_API_KEY BELUM DIISI"
        )

        return []


    query = SEARCHES.get(
        category
    )


    if not query:

        return []


    params = {

        "q":
            query,

        "lang":
            "en",

        "country":
            "us",

        "max":
            min(
                limit,
                10
            ),

        "apikey":
            GNEWS_API_KEY

    }


    try:

        response = requests.get(

            GNEWS_URL,

            params=params,

            timeout=15

        )


        print(
            f"📡 GNews HTTP: "
            f"{response.status_code}"
        )


        if response.status_code != 200:

            print(
                "❌ GNEWS ERROR:",
                response.text[:500]
            )

            return []


        data = response.json()


        articles = data.get(
            "articles",
            []
        )


        print(
            f"✅ GNews {category}: "
            f"{len(articles)} berita"
        )


        results = []


        for article in articles:

            results.append({

                "category":
                    category,

                "title":
                    article.get(
                        "title",
                        ""
                    ),

                "description":
                    article.get(
                        "description",
                        ""
                    ),

                "link":
                    article.get(
                        "url",
                        ""
                    ),

                "source_url":
                    article.get(
                        "url",
                        ""
                    ),

                "published":
                    article.get(
                        "publishedAt",
                        ""
                    ),

                "source_name":
                    get_source_name(
                        article
                    ),

                "source":
                    get_source_name(
                        article
                    )

            })


        return results


    except Exception as e:

        print(
            "❌ GNEWS REQUEST ERROR:",
            repr(e)
        )

        return []


# =========================================================
# GET ALL NEWS
# =========================================================

def get_all_news(
    limit_per_category=10
):

    print(
        "=========================================="
    )

    print(
        "📰 GNEWS FUNDAMENTAL ENGINE"
    )

    print(
        "=========================================="
    )


    all_news = []


    for category in SEARCHES:

        news = get_news(

            category,

            limit_per_category

        )


        all_news.extend(
            news
        )


    # =====================================================
    # REMOVE DUPLICATE
    # =====================================================

    unique = {}

    for item in all_news:

        title = item.get(
            "title",
            ""
        ).strip().lower()


        if title:

            unique[title] = item


    results = list(
        unique.values()
    )


    print(
        f"📰 TOTAL UNIQUE: "
        f"{len(results)}"
    )


    return results
