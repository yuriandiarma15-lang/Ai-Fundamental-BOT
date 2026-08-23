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
# ECONOMIC CALENDAR
# =========================================================

ECONOMIC_CALENDAR_API_KEY = os.getenv(
    "ECONOMIC_CALENDAR_API_KEY",
    ""
)


# =========================================================
# FUNDAMENTAL SETTINGS
# =========================================================

NEWS_PREPARE_MINUTES = 30


# Minimum impact
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

AREA_LOOKBACK = 100

ATR_PERIOD = 14

AREA_ATR_MULTIPLIER = 0.50


# =========================================================
# SCHEDULER
# =========================================================

SCHEDULER_INTERVAL_SECONDS = 30
