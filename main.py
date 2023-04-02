a = ['alina', 'katarzyna', 'maciek']
b = ['bartek', 'krzysiek', 'alina', 'maciek']
c = ['bartek', 'ania', 'kasia', 'alina']
a2=set(a)
b2=set(b)
c2=set(c)

suma = {*a2, *b2}
cz_wspolna = a2.intersection(b2)
print(cz_wspolna)
print(c2.difference(a2))
print(a2 &c2 & b2)
print(b2.difference(a2 & c2))
print(a2.union(b2, c2))
print(a2.difference(b2.union(c2)))