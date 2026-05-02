#first task
#name = input("Enter the Your Name : ")

#second task
#def my_name():
#name = input("Enter the Your Name : ")
#print("Hello " +name)

#3RD TASK
#taking user name and making uppercase
name = input("Enter the Your Name : ")
ls = name.upper()
name.upper()
print(f"Hello {ls}")

#4th task
#function to take userinput 
# def input_name():
#     firstname = input("Enter the Your First Name : ")
#     lastname = input("Enter the Your First Name : ")
#     schoolname = input("Enter the Your Name : ")
#     location  = input("Enter your the location: ")
    
#     print(f"Hello {firstname +" "+lastname} your school is {schoolname} and location is {location}  ")
    
# input_name()
# def take_userinput(): 
#     firstname = input("Enter the Your First Name : ")
#     lastname = input("Enter the Your First Name : ")
#     schoolname = input("Enter the Your School Name : ")
#     location  = input("Enter your the location: ")
    
#     return f"Hello {firstname +" "+lastname} your school name is {schoolname} and location is {location}  "

# print(take_userinput())
    
    #task 5
#dayofthe week condition
# def week_day():
#     day = input("Enter the day of the week :")
#     if day == "Monday":
#         print("Monday")
#     elif day == "Tuesday":
#         print("Tuesday")
#     elif day == "Wednesday":
#         print("Wednesday")
#     elif day == "Thursday":
#         print("Thursday")
#     elif day == "Firday":
#         print("Friday")  
#     elif day == "Saturday":
#         print("Saturday")  
#     elif day == "Sunday":
#         print("Sunday")
#     else:
#         print("Invalid") 
        
# week_day() 

#dayofthe week condition
# def week_day():
#     day = input("Enter the day of the week : ")
#     if day == "Monday":
#         return "Monday"
    
#     elif day == "Tuesday":
#         return "Tuesday"
    
#     elif day == "Wednesday":
#         return "Wednesday"
    
#     elif day == "Thursday":
#         return "Thursday"
    
#     elif day == "Firday":
#        return "Friday"  
   
#     elif day == "Saturday":
#         return "Saturday"
     
#     elif day == "Sunday":
#         return "Sunday"
    
#     else:
#         return "Invalid"
# print(week_day())

# def calcute():
#     a = float(input("Enter first number : "))
#     b = float(input("Enter second number : "))
#     c = input("Enter Rule ")
    
#     if c == "add":
#         return a + b
#     elif c == "sub":
#         return a - b
#     elif c == "mul":
#         return a * b
#     elif c == "div":
#         return a / b
#     else:
#         return "invalid input"
        
    

# print(calcute())

def whileloop():
    n = 0
    while n < 5:
        print("Meooow")
        n+=1
    
whileloop()   