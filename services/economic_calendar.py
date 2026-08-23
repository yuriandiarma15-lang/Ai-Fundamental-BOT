from dataclasses import dataclass
from datetime import datetime


@dataclass
class EconomicEvent:

    title: str

    event_time: datetime

    impact: str

    country: str = "US"

    forecast: str = "-"

    previous: str = "-"

    actual: str = "-"

    source_name: str = ""

    source_url: str = ""

    processed_prepare: bool = False

    processed_result: bool = False
