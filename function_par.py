def students(fullname, age, gender,course,school):
    print(f"{fullname} is {age} years of age persuing "
          f"{course} in {school} and gender {gender}")

students("Terry Waswa", 21, "Female", "Comp Science", "Emobilis")
students("Berryl Nabiswa", 18, "female", "beauty", "holy cress")

def square(num):
   return num**2
answer=square(9)
print(f"The square is {answer}")
