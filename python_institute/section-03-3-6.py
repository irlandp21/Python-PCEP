x = 4
y = 1

a = x & y # 4 & 1 = 0
b = x | y   # True
c = ~x  # tricky! True
d = x ^ 5 # False
e = x >> 2 # 1 = True
f = x << 2 # 8 = False

print(a, b, c, d, e, f)