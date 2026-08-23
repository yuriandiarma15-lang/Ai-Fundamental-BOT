from dataclasses import dataclass
from datetime import datetime


# =========================================================
# ECONOMIC EVENT
# =========================================================

@dataclass
class EconomicEvent:

    # =====================================================
    # IDENTITAS EVENT
    # =====================================================

    title: str

    event_time: datetime

    impact: str

    country: str = "US"


    # =====================================================
    # DATA EKONOMI
    # =====================================================

    forecast: str = "-"

    previous: str = "-"

    actual: str = "-"


    # =====================================================
    # SUMBER RESMI
    # =====================================================

    source_name: str = ""

    source_url: str = ""


    # =====================================================
    # STATUS PROCESS
    # =====================================================

    processed_prepare: bool = False

    processed_result: bool = False
