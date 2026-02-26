student=["sara","tharsi","siva","pallavi"]
subject=["maths","english","history","tamil"]
mark=[[58,86,78,76],[99,65,86,56],[59,98,79,80],[78,93,94,89]]
#print("\t\tsara\ttharsi\tsiva\tpallavi")
#print("maths\nenglish\nhistory\ntamil\ntotal\naverage")
print("student\tmaths\tenglish\thistory\ttamil")
for i in range(len(student)):
    total=average=0
    
  #  print(student[i],end="")
    for k in range(len(subject)):
        print(mark[i],end=" ")

