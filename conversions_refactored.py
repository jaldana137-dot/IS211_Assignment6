# conversions_refactored.py
# This is the refactored version of the conversion logic.
# Instead of a separate function for every pair of units,
# we use ONE convert() function that handles everything.
#
# The big idea: convert the input value to a common "base" unit first,
# then convert from that base unit to the target unit.
# For temperature, I'm using Celsius as the base.
# For distance, I'm using Meters as the base.
# This way we only need 2 steps no matter what units we're using.


# --- Custom Exception ---

class ConversionNotPossible(Exception):
    """Raised when the user tries to convert between incompatible unit types
    (like Celsius to Miles, which doesn't make sense)."""
    pass


# --- Conversion Tables ---

# These dicts define how to get FROM a unit TO the base unit.
# For temperature, base = Celsius.
# For distance, base = Meters.

# to_base_temp[unit] is a function that converts that unit to Celsius
to_base_temp = {
    "celsius":    lambda x: x,
    "fahrenheit": lambda x: (x - 32) * 5 / 9,
    "kelvin":     lambda x: x - 273.15,
}

# from_base_temp[unit] is a function that converts Celsius to that unit
from_base_temp = {
    "celsius":    lambda x: x,
    "fahrenheit": lambda x: (x * 9 / 5) + 32,
    "kelvin":     lambda x: x + 273.15,
}

# to_base_dist[unit] converts that unit to Meters
to_base_dist = {
    "miles":  lambda x: x * 1609.344,
    "yards":  lambda x: x * 0.9144,
    "meters": lambda x: x,
}

# from_base_dist[unit] converts Meters to that unit
from_base_dist = {
    "miles":  lambda x: x / 1609.344,
    "yards":  lambda x: x / 0.9144,
    "meters": lambda x: x,
}

# Group them together so we can figure out which "family" a unit belongs to
unit_families = [
    (to_base_temp, from_base_temp),
    (to_base_dist, from_base_dist),
]


# --- Main Function ---

def convert(fromUnit, toUnit, value):
    """
    Converts a value from one unit to another.

    Parameters:
        fromUnit (str): the unit we are converting from (e.g. "celsius")
        toUnit   (str): the unit we are converting to   (e.g. "kelvin")
        value  (float): the numeric value to convert

    Returns:
        float: the converted value

    Raises:
        ConversionNotPossible: if fromUnit and toUnit are not in the same
                               unit family (e.g. trying celsius -> miles)
    """
    # normalize to lowercase so capitalization doesn't matter
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    # look through each family to find one that contains BOTH units
    for to_base, from_base in unit_families:
        if fromUnit in to_base and toUnit in from_base:
            # step 1: convert from input unit to the base unit
            base_value = to_base[fromUnit](value)
            # step 2: convert from base unit to the target unit
            result = from_base[toUnit](base_value)
            return result

    # if we get here, the units are incompatible or unknown
    raise ConversionNotPossible(
        f"Cannot convert from '{fromUnit}' to '{toUnit}'. "
        f"They are either incompatible unit types or not supported."
    )
