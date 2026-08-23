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
# SOURCE NAME
# =========================================================

SOURCE_NAMES = {

    "FED":
        "Federal Reserve",

    "TREASURY":
        "U.S. Department of the Treasury",

    "BLS":
        "U.S. Bureau of Labor Statistics",

}


# =========================================================
# GET RSS NEWS
# =========================================================

def get_official_news(
    source_name: str,
    limit: int = 20
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

            title = item.get(
                "title",
                ""
            )

            link = item.get(
                "link",
                ""
            )

            published = item.get(
                "published",
                item.get(
                    "updated",
                    ""
                )
            )


            # =============================================
            # AMBIL SUMMARY
            # =============================================

            summary = item.get(
                "summary",
                ""
            )


            # =============================================
            # SIMPAN DATA
            # =============================================

            results.append({

                "source":
                    source_name,

                "source_name":
                    SOURCE_NAMES.get(
                        source_name,
                        source_name
                    ),

                "title":
                    title,

                "link":
                    link,

                "source_url":
                    link,

                "published":
                    published,

                "summary":
                    summary,

                # =========================================
                # ECONOMIC DATA
                #
                # RSS resmi biasanya tidak menyediakan
                # actual / forecast / previous.
                #
                # Default "-" agar tidak error.
                # =========================================

                "actual":
                    item.get(
                        "actual",
                        "-"
                    ),

                "forecast":
                    item.get(
                        "forecast",
                        "-"
                    ),

                "previous":
                    item.get(
                        "previous",
                        "-"
                    ),

            })


        return results


    except Exception as e:

        print(
            f"RSS ERROR [{source_name}]:",
            e
        )

        return []
