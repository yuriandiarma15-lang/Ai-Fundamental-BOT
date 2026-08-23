import requests

from config.settings import (
    GNEWS_API_KEY
)


# =========================================================
# GNEWS API
# =========================================================

GNEWS_URL = "https://gnews.io/api/v4/search"


# =========================================================
# SEARCH QUERY
# KHUSUS YANG RELEVAN TERHADAP XAU / USD
# =========================================================

SEARCHES = {

    "XAUUSD":
        'gold OR XAUUSD',

    "FED":
        '"Federal Reserve" OR FOMC OR Powell',

    "USD":
        '"US dollar" OR USD',

    "CPI":
        '"US CPI" OR inflation',

    "NFP":
        '"NFP" OR "nonfarm payrolls"',

    "PCE":
        '"US PCE" OR "PCE inflation"',

}


# =========================================================
# SOURCE NAME
# =========================================================

def get_source_name(
    article
):

    source = article.get(
        "source",
        {}
    )

    if isinstance(
        source,
        dict
    ):

        return source.get(
            "name",
            "GNews"
        )

    return "GNews"


# =========================================================
# GET GNEWS
# =========================================================

def get_news(
    category: str,
    limit: int = 10
):

    print(
        f"📰 GNEWS REQUEST: {category}"
    )


    # =====================================================
    # CHECK API KEY
    # =====================================================

    if not GNEWS_API_KEY:

        print(
            "❌ GNEWS_API_KEY BELUM DIISI"
        )

        return []


    # =====================================================
    # QUERY
    # =====================================================

    query = SEARCHES.get(
        category
    )


    if not query:

        print(
            f"❌ CATEGORY TIDAK DIKENAL: {category}"
        )

        return []


    # =====================================================
    # PARAMETER
    # =====================================================

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

        print(
            f"📡 Menghubungkan GNews: {category}"
        )


        response = requests.get(

            GNEWS_URL,

            params=params,

            timeout=15

        )


        print(
            f"📡 GNews HTTP: {response.status_code}"
        )


        # =================================================
        # ERROR
        # =================================================

        if response.status_code != 200:

            print(
                "❌ GNEWS ERROR:",
                response.text[:500]
            )

            return []


        # =================================================
        # JSON
        # =================================================

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


        # =================================================
        # PARSE ARTICLES
        # =================================================

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

                "content":
                    article.get(
                        "content",
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

                "source":
                    get_source_name(
                        article
                    ),

                "source_name":
                    get_source_name(
                        article
                    ),

                "image":
                    article.get(
                        "image",
                        ""
                    )

            })


        return results


    except requests.Timeout:

        print(
            f"⏱️ GNEWS TIMEOUT: {category}"
        )

        return []


    except requests.RequestException as e:

        print(
            "❌ GNEWS REQUEST ERROR:",
            repr(e)
        )

        return []


    except Exception as e:

        print(
            "❌ GNEWS ERROR:",
            repr(e)
        )

        return []


# =========================================================
# GET ALL RELEVANT NEWS
# =========================================================

def get_all_news(
    limit_per_category: int = 10
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


    categories = [

        "XAUUSD",

        "FED",

        "USD",

        "CPI",

        "NFP",

        "PCE",

    ]


    all_news = []


    for category in categories:

        news = get_news(

            category,

            limit_per_category

        )


        if news:

            all_news.extend(
                news
            )


    # =====================================================
    # REMOVE DUPLICATES
    # =====================================================

    unique = {}

    for item in all_news:

        title = item.get(
            "title",
            ""
        ).strip().lower()


        if not title:

            continue


        unique[title] = item


    results = list(
        unique.values()
    )


    print(
        f"📰 TOTAL GNEWS UNIQUE: "
        f"{len(results)}"
    )


    print(
        "=========================================="
    )


    return results
