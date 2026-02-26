"""
marks=[78,67,78,45,34,89,99,89]
m=set(marks)
print(m)
print(type(m))


a={1,2,3,4,5}
b={3,5,6,8,9,7}
c=a.union(b)#or a|b
print(c)
d=a.intersection(b)#or d=a&b
print(d)

#a={1,2,3,4,5}
#b={3,5,6,8,9,7}
e=a-b
print(e)
d=b-a
print(d)
m=a.symmetric_difference(b)
print(m)
"""

a={1,2,3}
b={1,2,3,4,5}
c={4,5,6}

c=a|b|c
print(c)#print order remove duplicates
d=a&b&c
print(d)
print(a>=b)#true or false
print(b.issuperset(a))
print(a.issuperset(b))
print(a<=b)