#Task
#create a calculator with three values
def calculator(num1, num2, operation="add"):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
       
        return num1 / num2
        
    else:
        return "Invalid operation"
    
print(calculator(2,2,"divide"))

# second method by Tutor
def calculatorT(a,b,c="add"):
    if c == "add":
        return a + b
    elif c=="sub":
        return a-b
    elif c=="div":
        return a/b
    else:
        return "Invalid"
    
print(calculatorT(4,6,"add"))
    