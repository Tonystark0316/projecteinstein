print("hello world")
print("meow meow")


def whileloop():
    n=0
    while n<5:
        print("meow")
        n+=1
whileloop()


def days_of_the_week(day):
    if day =="Monday":
        return("Monday")
    elif day =="Tuesday":
        return("Tuesday")
    elif day =="Wednesday":
        return("Wednesday")
    elif day =="Thursday":
        return("Thursday")
    elif day =="Friday":
        return("Friday")
    elif day =="Saturday":
        return("Saturday")
    elif day =="Sunday":
        return("Sunday")
    else:
       return "invalid input"
print(days_of_the_week("Friday"))
    
print("hello team")
print("meoow")


#simple_calculator
def calculator():
    print("simple calculator")
    print("operations: +,-,*,/,")
    num1 = float(input("Enter num1"))
    operator = input("Enter operator(+,-,/,*):")
    num2 = float(input("Enter num2"))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 !=0:
            result = num1/num2
        else:
            print("Error: division by zero not allowed")
            return
    else:
        print("Invalid operator")
        return
    print(f"Result{result}")
calculator()


def ussd():
    while True:
        print("1. Check Balance")
        print("2. Buy Airtime")
        print("3. exit")
        Select = int(input("select a choice"))
        if Select == 1:
            print("Your Balance is GHS 1000.00")
            input("\nPress Enter to continue...")
        elif Select == 2:
            Amount = int(input("Enter buy Airtime:"))
            print(f"You have successfully purchased GHS{Amount} Airtime!")
        elif Select == 3:
            print("Thank you for using KingTech services.Goodbye!")
            break
ussd()


# Months_of_the_year
def month_of_the_year():
    month = input(("Enter month"))
    if month == "January":
        return("January")
    elif month == "February":
        return("February")
    elif month == "March":
        return("March")
    elif month == "April":
        return("April")
    elif month == "May":
        return("May")
    elif month == "June":
        return("June")
    elif month == "July":
        return("July")
    elif month == "August":
        return("August")
    elif month == "September":
        return("September")
    elif month == "October":
        return("October")
    elif month == "November":
        return("November")
    elif month == "December":
        return("December")
    else:
        print("Invalid input")
        
month_of_the_year()

# Modulo_Arithmetic
def modulo_of_numbers():
    score = int(input("Input your score?"))
    if score%2 == 0:
        print("Odd")
    else:
        print("Even")
print(modulo_of_numbers())





    



