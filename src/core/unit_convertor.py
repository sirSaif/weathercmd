from .units import Unit

class UnitConverter:
    def __init__(self, parser_default_unit, dest_unit=None):
        self._parser_default_unit = parser_default_unit
        self.dest_unit = dest_unit

        self._convert_functions = {
            Unit.CELSIUS: self._to_celsius,
            Unit.FAHRENHEIT: self._to_fahrenheit,
        }
    @property
    def dest_unit(self):
        return self._dest_unit

    @dest_unit.setter
    def dest_unit(self, dest_unit):
        self._dest_unit = dest_unit

    def convert(self, temp):
        try:
            temperature = float(temp)
        except ValueError:
            return 0

        # no need for conversion
        if self.dest_unit == self._parser_default_unit or self.dest_unit is None:
            return self._format_results(temperature)

        func = self._convert_functions[self.dest_unit]
        converted_temperature = func(temperature)

        return self._format_results(converted_temperature)

    def _format_results(self, temprature):
        return int(temprature) if temprature.is_integer() else f'{temprature:.1f}'

    def _to_celsius(self, fahrenheit_temp):
        return (fahrenheit_temp - 32) * 5 / 9

    def _to_fahrenheit(self, celsius_temp):
        return (celsius_temp * 9 / 5) + 32