# =========================================================
# XAUUSD / USD HIGH IMPACT FILTER
# =========================================================

XAU_USD_KEYWORDS = [

    # =========================
    # FED / INTEREST RATE
    # =========================

    "fomc",
    "federal funds rate",
    "interest rate",
    "fed interest rate",
    "rate decision",
    "monetary policy",
    "powell",

    # =========================
    # INFLATION
    # =========================

    "cpi",
    "consumer price index",
    "core cpi",

    "ppi",
    "producer price index",
    "core ppi",

    "pce",
    "core pce",
    "personal consumption expenditures",

    # =========================
    # EMPLOYMENT
    # =========================

    "nonfarm payroll",
    "non-farm payroll",
    "nfp",

    "unemployment rate",
    "unemployment",

    "employment situation",
    "employment change",

    "initial jobless claims",
    "jobless claims",

    "jolts",

    # =========================
    # ECONOMIC GROWTH
    # =========================

    "gdp",
    "gross domestic product",

    # =========================
    # CONSUMPTION
    # =========================

    "retail sales",
    "consumer confidence",
    "consumer sentiment",

    # =========================
    # BUSINESS ACTIVITY
    # =========================

    "ism manufacturing",
    "ism services",
    "ism non-manufacturing",

    "manufacturing pmi",
    "services pmi",

]


def is_xau_usd_relevant(
    title: str
) -> bool:

    if not title:
        return False

    text = (
        title
        .lower()
        .strip()
    )

    for keyword in XAU_USD_KEYWORDS:

        if keyword in text:

            return True

    return False


def get_impact(
    title: str
) -> str:

    if not title:

        return "LOW"

    text = (
        title
        .lower()
        .strip()
    )

    high_keywords = [

        "fomc",
        "federal funds rate",
        "interest rate",
        "rate decision",

        "cpi",
        "consumer price index",

        "ppi",
        "producer price index",

        "nonfarm payroll",
        "non-farm payroll",
        "nfp",

        "unemployment rate",

        "pce",
        "core pce",

    ]

    for keyword in high_keywords:

        if keyword in text:

            return "HIGH"

    return "MEDIUM"
