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
# FUNDAMENTAL API
# =========================================================


# ---------------------------------------------------------
# GNEWS
# Berita terbaru yang berhubungan dengan USD / XAU
# ---------------------------------------------------------

GNEWS_API_KEY = os.getenv(
    "GNEWS_API_KEY",
    ""
)


# ---------------------------------------------------------
# BLS
# CPI
# PPI
# Employment
# Unemployment
# ---------------------------------------------------------

BLS_API_KEY = os.getenv(
    "BLS_API_KEY",
    ""
)


# ---------------------------------------------------------
# BEA
# PCE
# GDP
# Personal Income
# Consumer Spending
# ---------------------------------------------------------

BEA_API_KEY = os.getenv(
    "BEA_API_KEY",
    ""
)


# ---------------------------------------------------------
# FRED
# Federal Reserve Economic Data
# ---------------------------------------------------------

FRED_API_KEY = os.getenv(
    "FRED_API_KEY",
    ""
)


# ---------------------------------------------------------
# ALPHA VANTAGE
# Market / economic data
# ---------------------------------------------------------

ALPHA_VANTAGE_API_KEY = os.getenv(
    "ALPHA_VANTAGE_API_KEY",
    ""
)


# =========================================================
# ECONOMIC CALENDAR
# =========================================================

# Tidak digunakan untuk sementara.
#
# Economic Calendar berbayar tidak digunakan.
#
# Kita menggunakan:
# GNews  -> berita
# BLS    -> data ekonomi
# BEA    -> PCE / GDP
# FRED   -> data Federal Reserve
#
# Untuk saat ini tidak perlu API Calendar.

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
# IMPACT LEVEL
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


# =========================================================
# SCHEDULER
# =========================================================

SCHEDULER_INTERVAL_SECONDS = int(
    os.getenv(
        "SCHEDULER_INTERVAL_SECONDS",
        "30"
    )
)
