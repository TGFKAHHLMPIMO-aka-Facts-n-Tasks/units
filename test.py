from units import *

m = Dimension('m', 'meter')
s = Dimension('s', 'second')
kg = Dimension('kg', 'kilogram')


N = Quantity({kg: 1, m: 1, s: -2})
h = Quantity({s: 1}, 3600)
km = Quantity({m: 1}, 1e3)
l = Quantity({m: 3}, 1e-3)

kmh = Quantity({km: 1, h: -1})

print(N)
print(h)
print(km)
print(kmh)
print(l**3)
print(h * N)
print(3 * h)
print(h * 3)
print(1/h)
print(h/h)
print(km / 1e3)
print(Quantity(2))
print(Quantity())
print(l**'1/3')
print(km**(1/3))
print(km + m)
print(m-m)
print(1 - Quantity(1))
print(Quantity(3) - 2)
print(m + s)
