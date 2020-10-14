from .base_enum import BaseEnum
from enum import unique

@unique
class ForecastType(BaseEnum):
    TODAY = 'today'
    FIVEDAYS = '5day'
    TENDAYS = '10day'
    WEEKEND = 'weekend'