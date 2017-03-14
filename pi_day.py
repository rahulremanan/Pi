# a generator to approximate pi to n digits
# the result is a string
# tested with Python36
from mpmath import mp
mp.dps = 2017  # set number of digits
print(mp.pi)
