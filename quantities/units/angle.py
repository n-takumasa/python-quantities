# -*- coding: utf-8 -*-
"""
"""

from numpy import pi

from quantities.unitquantity import UnitAngle, UnitQuantity, dimensionless

radian = radians = UnitAngle(
    'radian',
    1*dimensionless,
    symbol='rad',
    aliases=['radians']
)
turn = revolution = cycle = turns = circle = circles = UnitAngle(
    'turn',
    2*pi*radian,
    aliases=['turns', 'revolutions', 'circles', 'cycles']
)
degree = arcdeg = arcdegree = angular_degree = UnitAngle(
    'arcdegree',
    pi/180*radian,
    symbol='deg',
    u_symbol='°',
    aliases=[
        'degree', 'degrees', 'arc_degree', 'arc_degrees', 'angular_degree',
        'angular_degrees', 'arcdegrees'
    ]
)
arcminute = arcmin = arc_minute = angular_minute = UnitAngle(
    'arcminute',
    arcdeg/60,
    symbol='arcmin',
    u_symbol='′',
    aliases=[
        'arcmin', 'arcmins', 'arcminutes', 'arc_minute', 'arc_minutes',
        'angular_minute', 'angular_minutes'
    ]
)
arcsecond = arcsec = arc_second = angular_second = UnitAngle(
    'arcsecond',
    arcmin/60,
    symbol='arcsec',
    u_symbol='″',
    aliases=[
        'arcsec', 'arcsecs', 'arcseconds', 'arc_second', 'arc_second',
        'angular_second', 'angular_seconds'
    ]
)
grad = grade = UnitAngle(
    'grad',
    0.9*arcdeg,
    aliases=['grads', 'grade', 'grades', 'gron', 'grons', 'gradian', 'gradians']
)

degrees_north = degrees_N = UnitAngle(
    'degrees_north',
    arcdeg,
    symbol='degN',
    u_symbol='°N',
    aliases=['degrees_N']
)
degrees_east = degrees_E = UnitAngle(
    'degrees_east',
    arcdeg,
    symbol='degE',
    u_symbol='°E',
    aliases=['degrees_E']
)
degrees_west = degrees_W = UnitAngle(
    'degrees_west',
    arcdeg,
    symbol='degW',
    u_symbol='°W',
    aliases=['degrees_W']
)
degrees_true = degrees_T = UnitAngle(
    'degrees_true',
    arcdeg,
    symbol='degT',
    u_symbol='°T',
    aliases=['degrees_T']
)

sr = steradian = UnitQuantity(
    'steradian',
    radian**2,
    symbol='sr',
    aliases=['steradians']
)

del UnitQuantity
