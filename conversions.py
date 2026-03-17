# conversions.py
# This file has all the temperature conversion functions
# for the assignment. Each one takes a float and returns
# the converted value as a float.


def convertCelsiusToKelvin(celsius):
    # formula: K = C + 273.15
    kelvin = celsius + 273.15
    return kelvin


def convertCelsiusToFahrenheit(celsius):
    # formula: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def convertFahrenheitToCelsius(fahrenheit):
    # formula: C = (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def convertFahrenheitToKelvin(fahrenheit):
    # convert to celsius first, then to kelvin
    celsius = convertFahrenheitToCelsius(fahrenheit)
    kelvin = convertCelsiusToKelvin(celsius)
    return kelvin


def convertKelvinToCelsius(kelvin):
    # formula: C = K - 273.15
    celsius = kelvin - 273.15
    return celsius


def convertKelvinToFahrenheit(kelvin):
    # convert to celsius first, then to fahrenheit
    celsius = convertKelvinToCelsius(kelvin)
    fahrenheit = convertCelsiusToFahrenheit(celsius)
    return fahrenheit
