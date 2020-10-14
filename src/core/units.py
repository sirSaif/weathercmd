from .base_enum import BaseEnum
from enum import unique, auto

@unique
class Unit(BaseEnum):
    CELSIUS = auto()
    FAHRENHEIT = auto()