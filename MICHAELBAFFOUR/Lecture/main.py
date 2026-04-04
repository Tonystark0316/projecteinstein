#Task 2
name = "Michael"
name = name + input ("taking name")
print(name)

#Task 2
#Writing function to call name
def name():
    name = input("What is your name?\n")
    print (f"Hello {name}")
name()

#Task 3
#Taking input and capitalizing
name = input('What is your name \n')
print (f'Hello {name.upper()}')

# Task 4
# A function taking username and concatenate
def take_name():
    name_1 = input('What is your name \n')
    name_2 = input('What is your last name \n')
    return f'this is your full name {name_1 +' '+ name_2}'
    
print(take_name())

#Task 5
#Take users day input

def check_days():
    day = input('Give the day of the week\n')
    if day == 'monday':
       return 'Monday'
    elif day == 'tuesday':
       return 'Tuesday'
    elif day == 'wednesday':
       return 'Wednesday'
    elif day == 'thursday':
      return 'Thursday'
    elif day == 'Friday' :
      return 'Friday'
    elif day == 'saturday':
      return 'Saturday'
    elif day == 'sunday':
      return 'Sunday'
    else:
       print('ERROR')
       

print(check_days())

#task 6
#Building a calculator

def build_cal():
   a = int(input('Enter your first number: '))
   b = int(input('Enter your second number: '))
   c = input('Enter operation: ')
   if c == 'add':
      return a + b
   elif c == 'mul':
      return a*b
   elif c == 'subt':
      return a - b
   elif c == 'div':
      return a/b
   else:
      print('error')

print(build_cal())

#Task 7
#Writing while loop
# n = 0
# while n < 5:
#     print('meow')
#     n += 1
    
   
   
