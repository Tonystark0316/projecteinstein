# #second task
# name = input ("what is your name : ")

# print("Hello " + name)

# #third task
# #capitalizing of input
# name = input ("Enter your name : ")
# print(f"hello {name.upper()}" )


# #users full name

# def input_name():
#   first_name = input("Enter your first name : ")
#   sur_name = input("Enter surname : ")
#   return( first_name + sur_name)

# input_name()

# def take_name():
#   first_name = input("Enter your first name : ")
#   sur_name = input("Enter last name : ")
#   return f"your fullname {first_name} + {sur_name}"

# take_name()

# #fifth task
# day = input(" Enter the day : ")

# #checking the day function

# def checking_day():

#   if day == "Monday":
#       return"Monday"
  
#   elif day == "Tuesday":
#      return"Tuesday"
  
#   elif day == "Wednessday":
#      return"Wednessday"
  
#   elif day == "Thursday":
#      return"Thursday"
  
#   elif day == "Friday":
#      return"Friday"
  
#   elif day == "Saturday":
#      return"Saturday"
  
#   elif day == "Sunday":
#      return"Sunday"
  
#   else:
#      return"invalid day"
  
#   print(checking_day())


#calculator
def calculator():
 
  num1 = int(input("Enter first number : "))
  num2 = int(input("Enter second number : "))
  rule = input("Enter rule : ")

  if rule == "add":
   return num1 + num2

  elif rule == "sub":
   return num1 - num2

  elif rule == "mul":
   return num1 * num2

  elif rule == "div":
   return num1 / num2 

  else:
   return "invalid"
#print(calculator())

def cat_sound():
 catcry = 0 
 while catcry < 5:
  print("meow")
  catcry += 1

cat_sound()
