
salary = [25000, 50000, 80000, 82000, 94000, 120000, 150000, 200000, 250000, 300000, 350000, 400000]
month = ["jan", "feb", "march", "apr", "may", "jun", "july", "aug", "sep", "oct", "nov", "dec"]

tax = 0
net_salary = 0
total_salary=0
total_tax=0
total_net_salry=0

i = 0
while i < len(salary):

    # tax rules
    if salary[i] <= 50000:
        tax = salary[i] * 3 / 100
    elif salary[i] <= 30000:
        tax = salary[i] * 5 / 100
    elif salary[i]<=300000:
        tax = salary[i]*8/100 
    else:
        tax = salary[i] * 10 / 100

    net_salary = salary[i] - tax

    print("month salary tax net_salary")
    print(f"{month[i]} {salary[i]} {tax} {net_salary}")

    i += 1
"""
sub=["maths","tamil","scince","scince","tamil","scince","maths","maths","maths"]
sub.append("tamil")
print(sub)
sub.insert(0,"scince")
print(sub)
sub.extend(["physics","biology"])
print(sub)
sub.pop()
print(sub)
sub.pop(2)
print(sub)
print(sub.index("maths"))
print(sub)

print(sub.count("maths"))
sub.clear()
print(sub)
#sub.remove("scince")
#print(sub)
print(sub[4])
"""