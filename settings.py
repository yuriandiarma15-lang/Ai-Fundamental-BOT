# =========================================================
# GNEWS
# =========================================================

GNEWS_API_KEY = os.getenv(
    "GNEWS_API_KEY",
    ""
)

GNEWS_REFRESH_MINUTES = int(
    os.getenv(
        "GNEWS_REFRESH_MINUTES",
        "60"
    )
)

GNEWS_LIMIT = int(
    os.getenv(
        "GNEWS_LIMIT",
        "10"
    )
)

# Jangan kirim semua berita ke Telegram.
GNEWS_MAX_TELEGRAM_NEWS = int(
    os.getenv(
        "GNEWS_MAX_TELEGRAM_NEWS",
        "5"
    )
)
