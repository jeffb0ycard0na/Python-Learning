a = b = c = d = 12
print(d)
a, b = 12, 12
print(a, b)
a, b = (b, a)
print("a is {}".format(a))
print("b is {}".format(b))
