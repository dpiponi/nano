metre = 1.0
meter = metre
nanometer = 1e-9*meter
nanometre = 1e-9*metre
second = 1.0
coulomb = 1.0
kg = 1.0
newton = kg*meter/(second**2)
joule = newton*meter
tesla = newton/(meter/second)/coulomb
c = 299792458*meter/second

electron_charge = 1.60217646e-19*coulomb
hbar = 1.054571726e-34*joule*second

# SCRATCHPAD
# It's tricky trying to resolve the different unit systems.
# I'm using SI units.
# e*phi/(hbar*c)

# T = kg/coulomb/s
#   = newton/meter*second/coulomb
#   = newton/(meter/second)/coulomb

# [e*phi/(hbar*c)]
# = coulomb*meter^2*tesla/(joule*second)/(meter/second)
# = coulomb*meter^2*newton/(meter/second)/coulomb/joule/second/(meter/second)
# = meter^2*newton/(meter/second)/joule/second/(meter/second)
# = meter*(newton*meter)/(meter/second)/(newton*meter)/second/(meter/second)
# = meter/(meter/second)/(meter/second)/second
# = second/meter

# [e*phi] = newton/(m/s)*m^2 = newton*m/s
# [hbar] = joule*s = newton*m*s
# [c] = m/s
# [e*phi/hbar/c] = newton*m/s/(newton*m*s)/(m/s)
#                = m/s/(m*s)/(m/s)
#                = 1/(m*s) ?????

# [hbar/e] = joule*second/coulomb
#          = newton*m*second/coulomb
#          = newton/coulomb/(m/s)*m^2
#          = [flux*area]

# e*phi/hbar is what I want???

# [e*phi/hbar] = coulomb * newton/(m/s)/coulomb * m^2 / joule / s
#              = newton/(m/s) * m^2 / (newton*m) /s
#              = 1/(m/s) * m^2 / (m) /s
#              = s/m * m^2 / (m) /s
#              = s * m / m /s
#              = 1 !!!!!!!!!!!!!!!!!!!!!
