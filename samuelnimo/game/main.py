import random
def main():
    #rock ,paper scissors
    values = ['rock','paper','scissors']
    take_input = input("Please Enter any of the list 'rock','paper','scissors' : " ).lower() 
    results = userinput(take_input,values)
    computer_cc = computer_choice(values)
    m_condition = main_condition(results,computer_cc)
    print("You choice is " + results + " And computer choice is " + computer_cc + " The result is " + m_condition)
    # print(computer_cc)
    # print(results)
    # print(m_condition)
      
      #userinput functon  
def userinput(take_input,values):
    #rock ,paper scissors
    while take_input not in values:
     take_input = input("Please Enter any of the list 'rock','paper','scissors' : " ).lower() 
    return take_input

#computer choice function
def computer_choice(values): 
    c_choice = random.choice(values)
    return c_choice
#condition function creating
def main_condition(userinput,computer_cc):
    
    if userinput == "rock" and computer_cc == "scissors":
        return "You have won"

    elif userinput == "rock" and computer_cc == "paper":
        return "You have won"
    
    elif userinput == "scissors" and computer_cc == "rock":
        return "You have loss"

    elif userinput == "paper" and computer_cc == "rock":
        return "You have loss"
    
    elif userinput == "scissors" and computer_cc == "paper":
        return "You have loss"
    
    elif userinput == "paper" and computer_cc == "scissors":
        return "You have loss"
    else:
        return "DRAW"

#calling the mainfunction  
main()