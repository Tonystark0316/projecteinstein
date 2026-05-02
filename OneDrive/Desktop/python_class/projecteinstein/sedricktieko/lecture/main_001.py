def take_name():
    first_name= input("What is your first name: ").upper()
    
    second_name= input("what is your second name: ").upper()
    fullname=first_name +" " + second_name
    return fullname

print(take_name())