import math

# Greatest common divisor
print(math.gcd(80, 64, 152))

# Least common multiple
print(math.lcm(4, 8, 5))

# Next float after 4 going towards 5
# 4.000000000000001
print(math.nextafter(4, 5))

# Next float after 9 going towards 0
# 8.999999999999998
print(math.nextafter(9, 0))

# Unit in the Last Place
# 0.125
print(math.ulp(1000000000000000))

# 4.440892098500626e-16
print(math.ulp(3.14159265))
