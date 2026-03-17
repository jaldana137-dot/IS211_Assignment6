# tests.py
# This file tests all 6 conversion functions from conversions.py
# I'm using a helper function to keep things clean and print results
# for every single test case like the assignment says.

import unittest
from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit,
)


# helper so I don't have to type round() everywhere
def r(value):
    return round(value, 2)


class TestCelsiusToKelvin(unittest.TestCase):

    def test_case_1(self):
        result = r(convertCelsiusToKelvin(0.0))
        print(f"  CelsiusToKelvin: 0.0 C => expected 273.15, got {result}")
        self.assertEqual(result, 273.15)

    def test_case_2(self):
        result = r(convertCelsiusToKelvin(100.0))
        print(f"  CelsiusToKelvin: 100.0 C => expected 373.15, got {result}")
        self.assertEqual(result, 373.15)

    def test_case_3(self):
        result = r(convertCelsiusToKelvin(300.0))
        print(f"  CelsiusToKelvin: 300.0 C => expected 573.15, got {result}")
        self.assertEqual(result, 573.15)

    def test_case_4(self):
        result = r(convertCelsiusToKelvin(-273.15))
        print(f"  CelsiusToKelvin: -273.15 C => expected 0.0, got {result}")
        self.assertEqual(result, 0.0)

    def test_case_5(self):
        result = r(convertCelsiusToKelvin(-40.0))
        print(f"  CelsiusToKelvin: -40.0 C => expected 233.15, got {result}")
        self.assertEqual(result, 233.15)


class TestCelsiusToFahrenheit(unittest.TestCase):

    def test_case_1(self):
        result = r(convertCelsiusToFahrenheit(0.0))
        print(f"  CelsiusToFahrenheit: 0.0 C => expected 32.0, got {result}")
        self.assertEqual(result, 32.0)

    def test_case_2(self):
        result = r(convertCelsiusToFahrenheit(100.0))
        print(f"  CelsiusToFahrenheit: 100.0 C => expected 212.0, got {result}")
        self.assertEqual(result, 212.0)

    def test_case_3(self):
        result = r(convertCelsiusToFahrenheit(300.0))
        print(f"  CelsiusToFahrenheit: 300.0 C => expected 572.0, got {result}")
        self.assertEqual(result, 572.0)

    def test_case_4(self):
        result = r(convertCelsiusToFahrenheit(-40.0))
        print(f"  CelsiusToFahrenheit: -40.0 C => expected -40.0, got {result}")
        self.assertEqual(result, -40.0)

    def test_case_5(self):
        result = r(convertCelsiusToFahrenheit(37.0))
        print(f"  CelsiusToFahrenheit: 37.0 C => expected 98.6, got {result}")
        self.assertEqual(result, 98.6)


class TestFahrenheitToCelsius(unittest.TestCase):

    def test_case_1(self):
        result = r(convertFahrenheitToCelsius(32.0))
        print(f"  FahrenheitToCelsius: 32.0 F => expected 0.0, got {result}")
        self.assertEqual(result, 0.0)

    def test_case_2(self):
        result = r(convertFahrenheitToCelsius(212.0))
        print(f"  FahrenheitToCelsius: 212.0 F => expected 100.0, got {result}")
        self.assertEqual(result, 100.0)

    def test_case_3(self):
        result = r(convertFahrenheitToCelsius(572.0))
        print(f"  FahrenheitToCelsius: 572.0 F => expected 300.0, got {result}")
        self.assertEqual(result, 300.0)

    def test_case_4(self):
        result = r(convertFahrenheitToCelsius(-40.0))
        print(f"  FahrenheitToCelsius: -40.0 F => expected -40.0, got {result}")
        self.assertEqual(result, -40.0)

    def test_case_5(self):
        result = r(convertFahrenheitToCelsius(98.6))
        print(f"  FahrenheitToCelsius: 98.6 F => expected 37.0, got {result}")
        self.assertEqual(result, 37.0)


class TestFahrenheitToKelvin(unittest.TestCase):

    def test_case_1(self):
        result = r(convertFahrenheitToKelvin(32.0))
        print(f"  FahrenheitToKelvin: 32.0 F => expected 273.15, got {result}")
        self.assertEqual(result, 273.15)

    def test_case_2(self):
        result = r(convertFahrenheitToKelvin(212.0))
        print(f"  FahrenheitToKelvin: 212.0 F => expected 373.15, got {result}")
        self.assertEqual(result, 373.15)

    def test_case_3(self):
        result = r(convertFahrenheitToKelvin(572.0))
        print(f"  FahrenheitToKelvin: 572.0 F => expected 573.15, got {result}")
        self.assertEqual(result, 573.15)

    def test_case_4(self):
        result = r(convertFahrenheitToKelvin(-40.0))
        print(f"  FahrenheitToKelvin: -40.0 F => expected 233.15, got {result}")
        self.assertEqual(result, 233.15)

    def test_case_5(self):
        result = r(convertFahrenheitToKelvin(98.6))
        print(f"  FahrenheitToKelvin: 98.6 F => expected 310.15, got {result}")
        self.assertEqual(result, 310.15)


class TestKelvinToCelsius(unittest.TestCase):

    def test_case_1(self):
        result = r(convertKelvinToCelsius(273.15))
        print(f"  KelvinToCelsius: 273.15 K => expected 0.0, got {result}")
        self.assertEqual(result, 0.0)

    def test_case_2(self):
        result = r(convertKelvinToCelsius(373.15))
        print(f"  KelvinToCelsius: 373.15 K => expected 100.0, got {result}")
        self.assertEqual(result, 100.0)

    def test_case_3(self):
        result = r(convertKelvinToCelsius(573.15))
        print(f"  KelvinToCelsius: 573.15 K => expected 300.0, got {result}")
        self.assertEqual(result, 300.0)

    def test_case_4(self):
        result = r(convertKelvinToCelsius(0.0))
        print(f"  KelvinToCelsius: 0.0 K => expected -273.15, got {result}")
        self.assertEqual(result, -273.15)

    def test_case_5(self):
        result = r(convertKelvinToCelsius(233.15))
        print(f"  KelvinToCelsius: 233.15 K => expected -40.0, got {result}")
        self.assertEqual(result, -40.0)


class TestKelvinToFahrenheit(unittest.TestCase):

    def test_case_1(self):
        result = r(convertKelvinToFahrenheit(273.15))
        print(f"  KelvinToFahrenheit: 273.15 K => expected 32.0, got {result}")
        self.assertEqual(result, 32.0)

    def test_case_2(self):
        result = r(convertKelvinToFahrenheit(373.15))
        print(f"  KelvinToFahrenheit: 373.15 K => expected 212.0, got {result}")
        self.assertEqual(result, 212.0)

    def test_case_3(self):
        result = r(convertKelvinToFahrenheit(573.15))
        print(f"  KelvinToFahrenheit: 573.15 K => expected 572.0, got {result}")
        self.assertEqual(result, 572.0)

    def test_case_4(self):
        result = r(convertKelvinToFahrenheit(233.15))
        print(f"  KelvinToFahrenheit: 233.15 K => expected -40.0, got {result}")
        self.assertEqual(result, -40.0)

    def test_case_5(self):
        result = r(convertKelvinToFahrenheit(310.15))
        print(f"  KelvinToFahrenheit: 310.15 K => expected 98.6, got {result}")
        self.assertEqual(result, 98.6)


# ---------------------------------------------------------------
# Part IV tests — testing the refactored convert() function
# ---------------------------------------------------------------

from conversions_refactored import convert, ConversionNotPossible


class TestRefactoredTemperature(unittest.TestCase):
    """Make sure all temperature conversions work through convert()"""

    def test_celsius_to_fahrenheit(self):
        result = round(convert("celsius", "fahrenheit", 0.0), 2)
        print(f"  convert celsius->fahrenheit: 0.0 => expected 32.0, got {result}")
        self.assertEqual(result, 32.0)

    def test_celsius_to_kelvin(self):
        result = round(convert("celsius", "kelvin", 100.0), 2)
        print(f"  convert celsius->kelvin: 100.0 => expected 373.15, got {result}")
        self.assertEqual(result, 373.15)

    def test_fahrenheit_to_celsius(self):
        result = round(convert("fahrenheit", "celsius", 212.0), 2)
        print(f"  convert fahrenheit->celsius: 212.0 => expected 100.0, got {result}")
        self.assertEqual(result, 100.0)

    def test_fahrenheit_to_kelvin(self):
        result = round(convert("fahrenheit", "kelvin", 32.0), 2)
        print(f"  convert fahrenheit->kelvin: 32.0 => expected 273.15, got {result}")
        self.assertEqual(result, 273.15)

    def test_kelvin_to_celsius(self):
        result = round(convert("kelvin", "celsius", 0.0), 2)
        print(f"  convert kelvin->celsius: 0.0 => expected -273.15, got {result}")
        self.assertEqual(result, -273.15)

    def test_kelvin_to_fahrenheit(self):
        result = round(convert("kelvin", "fahrenheit", 373.15), 2)
        print(f"  convert kelvin->fahrenheit: 373.15 => expected 212.0, got {result}")
        self.assertEqual(result, 212.0)


class TestRefactoredDistance(unittest.TestCase):
    """Make sure all distance conversions work through convert()"""

    def test_miles_to_meters(self):
        result = round(convert("miles", "meters", 1.0), 3)
        print(f"  convert miles->meters: 1.0 => expected 1609.344, got {result}")
        self.assertEqual(result, 1609.344)

    def test_miles_to_yards(self):
        result = round(convert("miles", "yards", 1.0), 2)
        print(f"  convert miles->yards: 1.0 => expected 1760.0, got {result}")
        self.assertAlmostEqual(result, 1760.0, places=1)

    def test_yards_to_meters(self):
        result = round(convert("yards", "meters", 1.0), 4)
        print(f"  convert yards->meters: 1.0 => expected 0.9144, got {result}")
        self.assertEqual(result, 0.9144)

    def test_yards_to_miles(self):
        result = round(convert("yards", "miles", 1760.0), 2)
        print(f"  convert yards->miles: 1760.0 => expected 1.0, got {result}")
        self.assertAlmostEqual(result, 1.0, places=2)

    def test_meters_to_miles(self):
        result = round(convert("meters", "miles", 1609.344), 2)
        print(f"  convert meters->miles: 1609.344 => expected 1.0, got {result}")
        self.assertAlmostEqual(result, 1.0, places=2)

    def test_meters_to_yards(self):
        result = round(convert("meters", "yards", 0.9144), 2)
        print(f"  convert meters->yards: 0.9144 => expected 1.0, got {result}")
        self.assertAlmostEqual(result, 1.0, places=2)


class TestRefactoredSameUnit(unittest.TestCase):
    """Converting a unit to itself should always return the same value"""

    def test_celsius_to_celsius(self):
        result = convert("celsius", "celsius", 42.0)
        print(f"  convert celsius->celsius: 42.0 => expected 42.0, got {result}")
        self.assertEqual(result, 42.0)

    def test_fahrenheit_to_fahrenheit(self):
        result = convert("fahrenheit", "fahrenheit", 98.6)
        print(f"  convert fahrenheit->fahrenheit: 98.6 => expected 98.6, got {result}")
        self.assertEqual(result, 98.6)

    def test_kelvin_to_kelvin(self):
        result = convert("kelvin", "kelvin", 300.0)
        print(f"  convert kelvin->kelvin: 300.0 => expected 300.0, got {result}")
        self.assertEqual(result, 300.0)

    def test_miles_to_miles(self):
        result = convert("miles", "miles", 5.0)
        print(f"  convert miles->miles: 5.0 => expected 5.0, got {result}")
        self.assertEqual(result, 5.0)

    def test_yards_to_yards(self):
        result = convert("yards", "yards", 100.0)
        print(f"  convert yards->yards: 100.0 => expected 100.0, got {result}")
        self.assertEqual(result, 100.0)

    def test_meters_to_meters(self):
        result = convert("meters", "meters", 1.0)
        print(f"  convert meters->meters: 1.0 => expected 1.0, got {result}")
        self.assertEqual(result, 1.0)


class TestRefactoredIncompatible(unittest.TestCase):
    """Trying to mix temperature and distance should raise ConversionNotPossible"""

    def test_celsius_to_miles(self):
        print("  Testing celsius->miles raises ConversionNotPossible...")
        with self.assertRaises(ConversionNotPossible):
            convert("celsius", "miles", 100.0)

    def test_kelvin_to_yards(self):
        print("  Testing kelvin->yards raises ConversionNotPossible...")
        with self.assertRaises(ConversionNotPossible):
            convert("kelvin", "yards", 300.0)

    def test_fahrenheit_to_meters(self):
        print("  Testing fahrenheit->meters raises ConversionNotPossible...")
        with self.assertRaises(ConversionNotPossible):
            convert("fahrenheit", "meters", 32.0)

    def test_miles_to_celsius(self):
        print("  Testing miles->celsius raises ConversionNotPossible...")
        with self.assertRaises(ConversionNotPossible):
            convert("miles", "celsius", 5.0)

    def test_meters_to_kelvin(self):
        print("  Testing meters->kelvin raises ConversionNotPossible...")
        with self.assertRaises(ConversionNotPossible):
            convert("meters", "kelvin", 1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
