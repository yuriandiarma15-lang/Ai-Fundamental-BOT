from services.news_sources import (
    get_official_news
)


# =========================================================
# OFFICIAL SOURCES
# =========================================================

def collect_official_news():

    sources = [
        "FED",
        "TREASURY",
        "BLS"
    ]

    all_news = []

    for source in sources:

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
                f"NEWS SOURCE ERROR [{source}]:",
                e
            )

    return all_news


# =========================================================
# HIGH IMPACT KEYWORDS
# KHUSUS YANG RELEVAN TERHADAP USD / XAUUSD
# =========================================================

HIGH_IMPACT_KEYWORDS = [

    # =====================================================
    # FED / MONETARY POLICY
    # =====================================================

    "fomc",

    "fomc meeting",

    "fomc statement",

    "fomc minutes",

    "federal funds rate",

    "federal funds",

    "interest rate decision",

    "interest rate",

    "fed rate",

    "rate decision",

    "monetary policy",

    "monetary policy statement",

    "powell",

    "jerome powell",

    "fed chair",

    "fed chairman",

    "fed speech",

    "federal reserve speech",

    "beige book",


    # =====================================================
    # INFLATION
    # =====================================================

    "consumer price index",

    "cpi",

    "core cpi",

    "inflation",

    "pce",

    "core pce",

    "personal consumption expenditures",

    "producer price index",

    "ppi",

    "core ppi",


    # =====================================================
    # EMPLOYMENT
    # =====================================================

    "nonfarm payroll",

    "non-farm payroll",

    "nonfarm employment",

    "nfp",

    "unemployment rate",

    "unemployment",

    "employment report",

    "employment situation",

    "jobless claims",

    "initial jobless claims",

    "continuing jobless claims",

    "adp employment",

    "adp national employment",

    "average hourly earnings",

    "hourly earnings",


    # =====================================================
    # ECONOMIC GROWTH
    # =====================================================

    "gross domestic product",

    "gdp",

    "retail sales",

    "core retail sales",

    "durable goods",

    "durable goods orders",

    "industrial production",

    "capacity utilization",


    # =====================================================
    # BUSINESS ACTIVITY
    # =====================================================

    "ism manufacturing",

    "ism services",

    "ism non-manufacturing",

    "pmi",

    "manufacturing pmi",

    "services pmi",


    # =====================================================
    # CONSUMER / ECONOMIC SENTIMENT
    # =====================================================

    "consumer confidence",

    "consumer sentiment",

    "michigan consumer sentiment",

    "michigan sentiment",

]


# =========================================================
# EXCLUDE KEYWORDS
#
# Berita yang mengandung kata FED tetapi bukan economic
# event yang relevan terhadap XAUUSD.
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

    "bank holding",

    "financial institution",

    "deutsche bank",

    "national westminster",

    "bancshares",

]


# =========================================================
# CHECK HIGH IMPACT
# =========================================================

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

    # =====================================================
    # EXCLUDE TERLEBIH DAHULU
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
# FIND HIGH IMPACT NEWS
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

        if not is_high_impact_news(
            title
        ):

            continue

        # =================================================
        # HINDARI DUPLICATE
        # =================================================

        normalized_title = (
            title
            .lower()
            .strip()
        )

        if normalized_title in seen:

            continue

        seen.add(
            normalized_title
        )

        # =================================================
        # MARK HIGH IMPACT
        # =================================================

        news["impact"] = "HIGH"

        results.append(
            news
        )

    return results
