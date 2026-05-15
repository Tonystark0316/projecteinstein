#first task
username = input("What is your name? : ")
print (username)

#2nd task
name = input('What is your name? : ' )
print ('hello ' + name)

#3rd task
Capitaliszation of first letter of user's name
name = input('What is your name? : ') 
print (f'Hello {name.capitalize()}')

#4th task
Capitalization of ALL letters
name = input('What is your name? : ').upper()
print (f'Hello {name}')

#5th task
#A function that returns a user's full name
first_name = ""
surname = ""
def name_input():
    fname = input('What is your first name? : ')
    return fname
def name2_input():
    sname = input('What is your surname? : ')
    return sname

firstname = name_input()
surname = name2_input()
print(f'Fullname: {firstname.capitalize()} {surname.capitalize()}')

#6th task
#Conditions
day = input ('Enter day of the week? : ')

def check_day(day):
    if day == 'monday':
        return 'Monday'

    elif day == 'tuesday':
        return 'Tuesday'
    
    elif day == 'wednesday':
        return 'Wednesday'
    
    elif day == 'thurday':
        return 'Thursday'
    
    elif day == 'friday':
        return 'Friday'
    
    elif day == 'saturday':
        return 'Saturday'
    
    elif day == 'sunday':
        return 'Sunday'
    
    else:
        return f'Invalid, Not a day of the week'

#7th task
def cal():
    a=int(input('enter 1st number : '))
    b=int(input('enter 2nd number : '))
    c=input('enter operation : ')
    if c == 'add' or c == '+':
        return a + b
    elif c == 'sub'or c == '-':
        return a - b
    elif c == 'div' or c == '/':
        return a / b
    elif c == 'mul'or c == '*':
        return a * b
    elif c == 'mod' or c == '%':
        return a % b

    else:
        return f'cannot perform calculation' 


print (cal())

#8th task
#While loop
sound = 0
while sound < 10 :
    print (f'meow')
    sound += 2



