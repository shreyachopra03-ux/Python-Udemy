# Real Numbers (when i want precision in my program)

import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.4988989389

print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")
print(f"Difference temp: {ideal_temp - current_temp}")
print(sys.float_info)