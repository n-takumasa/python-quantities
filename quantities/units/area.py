"""
"""

from quantities.units.unitquantity import UnitQuantity
from quantities.units.length import m, rod

are = ares = UnitQuantity(
    'are',
    100*m**2,
    symbol='a',
    aliases=['ares']
)
b = barn = UnitQuantity(
    'barn',
    1e-28*m**2,
    symbol='b',
    aliases=['barnes']
)
cmil = circular_mil = UnitQuantity(
    'circular_mil',
    5.067075e-10*m**2,
    symbol='cmil',
    aliases=['circular_mils']
) # approximate, area of a circle with diameter=1 mil
D = darcy = UnitQuantity(
    'darcy',
    9.869233e-13*m**2,
    symbol='D'
)
mD = millidarcy = UnitQuantity(
    'millidarcy',
    9.869233e-10*m**2,
    symbol='mD'
)
ha = hectare = UnitQuantity(
    'hectare',
    10000*m**2,
    symbol='ha',
    aliases=['hectare']
)
acre = international_acre = UnitQuantity(
    'acre',
    4046.8564224*m**2,
    aliases=['acres', 'international_acre', 'international_acres']
) # exact: http://en.wikipedia.org/wiki/Acre
US_survey_acre = UnitQuantity(
    'US_survey_acre',
    160*rod**2,
    aliases=['US_survey_acres'],
)

del UnitQuantity, m, rod
