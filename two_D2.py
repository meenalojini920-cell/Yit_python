name=["meena","tharsi","sara"]#create name and subject list
subject=["english","tamil","history"]
marks=[
       [67,88,74],
       [56,67,87],
       [99,88,98]
]#mark 2D
print("student\tenglish\ttamil\thistory\ttotal\taverage\tgrade\tresult")#create a head line

for i in range(len(name)):#row
    total=0
    print(name[i],end="\t\t")
    
    for m in range(len(subject)):#for each subject mark
        print(marks[i][m],end="\t")
        total +=marks[i][m]
    average = total/len(subject)
    
    if average>80:
        grade="A"
    elif average<=70:
        grade="B"
    elif average<=55:
        grade="C"
    elif average<=45:
        grade="S"
    else:
        grade="F"
    
    print(total,end="\t")
    print(f"{average:.2f}",end="\t")
    print(grade)
    
      
    
