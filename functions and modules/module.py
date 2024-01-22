## import module_name
# option 1
import math
a = math.sin(60)
b = math.sqrt(100)

# option 2
from math import *
a = sin(60)
b = sqrt(100)

# option 3
from math import sqrt
a = sqrt(100)

# import user - defined module
from calc import *
a = total(4,5)
b = multiply(4,5)