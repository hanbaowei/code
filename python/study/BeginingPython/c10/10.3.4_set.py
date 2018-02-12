s = set(range(10))
print s

a = set([1,2,3])
b = set([2,3,4])

print a.union(b)
print a&b
c = a&b
print c.issubset(b)
print a.copy()
