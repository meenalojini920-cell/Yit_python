d={"name:":"seelan","age:":39,"gender:":"male"}
"""
key=d.keys()
print(key)
value=d.values()
print(value)
item=d.items()
print(item)

for key in d.keys():
    print(key,d[key])

for value in d.values():
    print(value)

for key,item in d.items():
    print(key,value)
"""
print(d)
d1=d.copy()
d1={"name:":"meena","age:":23,"gender:":"female"}
print(d1)