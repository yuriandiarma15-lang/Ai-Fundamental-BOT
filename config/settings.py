import os

from dotenv import load_dotenv


load_dotenv()


# =========================================================
# BOT
# =========================================================

BOT_TOKEN = os.getenv(
    "BOT_TOKEN",
    ""
)

ADMIN_USERNAME = os.getenv(
    "ADMIN_USERNAME",
    ""
)


# =========================================================
# ADMIN CHAT
# =========================================================

ADMIN_CHAT_ID = os.getenv(
    "ADMIN_CHAT_ID",
    ""
)


# =========================================================
# TIMEZONE
# =========================================================

TIMEZONE = os.getenv(
    "TIMEZONE",
    "Asia/Jakarta"
)


# =========================================================
# MARKET DATA
# =========================================================

TWELVE_DATA_API_KEY = os.getenv(
    "TWELVE_DATA_API_KEY",
    ""
)


# =========================================================
# GNEWS
# =========================================================

GNEWS_API_KEY = os.getenv(
    "GNEWS_API_KEY",
    ""
)


# =========================================================
# FUNDAMENTAL API
# =========================================================

BLS_API_KEY = os.getenv(
    "BLS_API_KEY",
    ""
)

BEA_API_KEY = os.getenv(
    "BEA_API_KEY",
    ""
)

FRED_API_KEY = os.getenv(
    "FRED_API_KEY",
    ""
)

ALPHA_VANTAGE_API_KEY = os.getenv(
    "ALPHA_VANTAGE_API_KEY",
    ""
)


# =========================================================
# ECONOMIC CALENDAR
# =========================================================

ECONOMIC_CALENDAR_API_KEY = os.getenv(
    "ECONOMIC_CALENDAR_API_KEY",
    ""
)


# =========================================================
# FUNDAMENTAL SETTINGS
# =========================================================

NEWS_PREPARE_MINUTES = int(
    os.getenv(
        "NEWS_PREPARE_MINUTES",
        "30"
    )
)


# =========================================================
# NEWS REFRESH
#
# GNews hanya dipanggil 1x setiap 60 menit
# =========================================================

NEWS_REFRESH_SECONDS = int(
    os.getenv(
        "NEWS_REFRESH_SECONDS",
        "3600"
    )
)


# =========================================================
# SCHEDULER
#
# Internal checking tetap setiap 30 detik
# =========================================================

SCHEDULER_INTERVAL_SECONDS = int(
    os.getenv(
        "SCHEDULER_INTERVAL_SECONDS",
        "30"
    )
)


# =========================================================
# IMPACT
# =========================================================

HIGH_IMPACT = "HIGH"

MEDIUM_IMPACT = "MEDIUM"

LOW_IMPACT = "LOW"


# =========================================================
# XAUUSD
# =========================================================

SYMBOL = "XAUUSD"


# =========================================================
# PRICE AREA
# =========================================================

AREA_LOOKBACK = int(
    os.getenv(
        "AREA_LOOKBACK",
        "100"
    )
)

ATR_PERIOD = int(
    os.getenv(
        "ATR_PERIOD",
        "14"
    )
)

AREA_ATR_MULTIPLIER = float(
    os.getenv(
        "AREA_ATR_MULTIPLIER",
        "0.50"
    )
)
