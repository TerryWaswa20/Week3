#list mutable ordered

mylist = ["Terry", "Cherry", "Berry", "Branny"]
mylist2 = [89, 12, 45, 0, 31, 15, -19]
mylist.sort()
mylist2.sort()

print(mylist)
print(f"My name is {mylist[0]}")
print("My name is " +mylist[0])
print(f"My sorted list {mylist2}")

#tupple immutable ordered
my_tupple = ("Kenya", "Uganda", "Tanzania", "Ethiopia")
print(my_tupple)
print(f"My country is {my_tupple[0]}")

#set ordered

fruits = {"oranges", "bananas", "pineaples", "Apples"}
print(fruits)

#dictionary

employees = {"Name": "Terry", "Age": 21, "Gender": "Female", "Salary": 200000}
print("Employyee's name :%s" % employees["Name"])
print("Employyee's age :%s" % employees["Age"])
