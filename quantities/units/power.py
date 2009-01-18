"""
"""

from quantities.unitquantity import UnitQuantity
from quantities.units.energy import Btu, J
from quantities.units.time import s, h, min
from quantities.units.electromagnetism import A, V
from quantities.units.length import ft
from quantities.units.force import lbf


W = watt = volt_ampere = UnitQuantity(
    'watt',
    J/s,
    symbol='W',
    aliases=['watts', 'volt_ampere', 'volt_amperes', 'VA']
)
mW = milliwatt = UnitQuantity(
    'milliwatt',
    W/1000,
    symbol='mW',
    aliases=['milliwatts']
)
kW = kilowatt = UnitQuantity(
    'kilowatt',
    1000*W,
    symbol='kW',
    aliases=['kilowatts']
)
MW = megawatt = UnitQuantity(
    'megawatt',
    1000*kW,
    symbol='mW',
    aliases=['megawatts']
)
hp = horsepower = UK_horsepower = British_horsepower = UnitQuantity(
    'horsepower',
    33000*ft*lbf/min,
    symbol='hp',
    aliases=['UK_horsepower', 'British_horsepower']
)
boiler_horsepower = UnitQuantity(
    'boiler_horsepower',
    33475*Btu/h
)
metric_horsepower = UnitQuantity(
    'metric_horsepower',
    0.73549875*kW
) # exact
electric_horsepower = UnitQuantity(
    'electric_horsepower',
    746*W
)
water_horsepower = UnitQuantity(
    'water_horsepower',
    746.043*W
) # exact

refrigeration_ton = ton_of_refrigeration = UnitQuantity(
    'refrigeration_ton',
    12000*Btu/h,
    aliases=['ton_of_refrigeration']
)

del UnitQuantity, Btu, J, s, h, A, V
