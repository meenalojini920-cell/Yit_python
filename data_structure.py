"""
subject=["maths","science","tamil","ICT"]
print(subject)
print(type(subject))
print(subject[0])
print(subject[-1])
print(len(subject))
subject[0]="History"
print(subject.append("physics"))

print("")
i=0
while i<len(subject):
    print(subject[i])
    i+=1
print("")    
 
marks1=(75,45,56)
marks2=(50,45,78)
marks3=marks1+marks2
print(marks3) 
"""
marks=(45,67,57)
a,*b,c=marks
print(a)
print(b)
print(c)
print(" ")
marks=(78,47,90,67,55)
*a,b,c=marks
print(a)
print(b)
print(c)