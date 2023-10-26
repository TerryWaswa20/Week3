#name = "terry"

fruits =["Mangoes", "Apples", "Oranges"]
try:
    for i in range(5):
        print(f"The index and element from the list is {i,fruits[i]}")
except:
    print("index out of range")

number = [3,5,7,9]
if len(number)>3:
    raise Exception(f"length of the given list must be less or equal to 3 but its{len(number)}")