# Take user input and save as ...
name = input("Enter your name: ")
print(name)

#Second Task

name = input("Enter your name: ")
print(f' Hello: {name}')

#Task 3
# Capitalize name: Solution one
name = input("Enter your name: ").upper()
#name=name.upper()
print(f' Hello: {name}')

# Capitalize name: Solution two
name = input("Enter your name: ")
name=name.upper()
print(f' Hello: {name}')

#Task 4
#REmove white space
name = input("What is your name: ").strip()
print(f' My name is: {name}')


#Task 4
# function that takes users fullname
def my_fullname():  
    first_name = input("What is your firstname: ")
    sur_name =input("What is your surname: ")
    fullname = first_name + " " + sur_name
    return (f' My Fullname is: {fullname.upper()}')

print(my_fullname())
