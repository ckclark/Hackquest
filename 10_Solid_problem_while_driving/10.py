from math import pi, sin
r = 6370.
d1 = 2 * r * sin(150. / 180 * pi / 2)
d2 = r * (150. / 180 * pi)
print int(d1), int(d2 / 200)
