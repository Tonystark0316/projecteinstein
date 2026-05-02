# take you full name
def take_name():
    first_name= input("what is your first name: ").lower()
    
    second_name= input("what is your second name: ").lower()
    
    return first_name,second_name
print(take_name())