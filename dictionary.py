
"""
data={
    "name":"seelan",
    "age":39,
    "gender":"male"
    }
print(data)
print(type(data))
print("*********")
"""

d=[("name","seelan"),("age",39),("gender","male")]
data=dict(d)
print(data)
print(type(d))
print(data["name"])
#print(data["grade"])#keyerror
print(data["age"])
print(data["gender"])
print(data.get("grade"))#none
print(data.get("gender"))
print(data.get("age"))
print("")

data["NIC"]=198742586
print(data)
print(data.update({"age":40,"NIC":19874227886}))
#assing defult value
print(data.get("dob","2002/06/08"))
del data["name"]#remove first key:value
print(data)
print(data.pop("NIC"))#remove mention key:value
print(data.popitem())#remove last items
print(data.clear())#clear all items 
