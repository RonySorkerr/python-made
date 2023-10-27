"""
what is a string formatting?
formatting in a well buffering menner the string is call string formatting.
showing the value in a well decent way is good enough for the user and the owner.
this is why string formatting matters.
"""
name = input("Etner your name : ")
age = input("Enter you age : ")
gpa = float(input("Enter you GPA : "))

print(f"Your name is {name} . You are {age} years old. Your GPA  is {gpa}")  # this is okey.
print("your name is ", name, "you are ", age, "years old. Your gpa is ", gpa)  # this is also okey

# showing the value in a single line
nama = "nony"
namba = 1318630366
print(nama , end=" ")
print(namba)
