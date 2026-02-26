x=[
    [10,20,30],
    [40,70,80],
    [25,35,16]
]
"""
print(x)
print(type(x))    
print(x[0][0])
print(x[0][1])
print(x[0][0])
print("")
print(x[1][0])
print(x[1][1])
print(x[1][2])
print("")
print(x[2][0])
print(x[2][1])
print(x[2][1])
"""
i=0
while i<len(x):
    y=0
    while y<len(x[i]):
        print(f"x[{i}][{y}]:{x[i][y]}",end="")
        y+=1
    i+=1        

   