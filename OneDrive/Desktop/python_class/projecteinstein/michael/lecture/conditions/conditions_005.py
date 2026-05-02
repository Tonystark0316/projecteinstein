

# second method by Tutor
def calculator(a,b,c="add"):
num1=input("Type the first Number: ")
num2=input("Type the second Number: ")
operant=input("Type the operant: ")
    if c == "add":
        return a + b
    elif c=="sub":
        return a-b
    elif c=="div":
        return a/b
    else:
        return "Invalid"
    
print(calculator())