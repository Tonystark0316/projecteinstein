import random 

def main():
    state = ['rock', 'paper', 'scissors' ]
    user_input = input("Enter one item : ")
    human = take_userinput(user_input, state)
    computer = make_computer_choice(state)
    m_condition = condition(human, make_computer_choice )
    print("you choice is " + human + " computer choice is " +  computer + " the resuls is " + m_condition)
    
    
def take_userinput(user_input, state):
   #pass
   #rock, paper, scissors
        while user_input not in state:
            user_input = input("choose one of the items (rock, paper, scissors) : ")
        return user_input
 
def condition(user_input, computer_choice):
    if user_input == "rock" and computer_choice == "scissors":
        return "won"
    elif user_input == "scissors" and computer_choice == "paper" :
        return "won"
    elif user_input == "paper" and computer_choice == "rock":
        return "won"
    elif user_input == "scissors" and computer_choice == "rock" :
        return "loss"
    elif user_input == "rock" and computer_choice == "paper" :
        return "loss"
    elif user_input == "paper" and computer_choice == "scissors" :
        return "loss"
    else :
        return "tie"
   

def make_computer_choice(state):
    computer_choice = random.choice(state)
    return computer_choice

main()


import random


def main():
    guess = list(range(1, 21))
    user_input = int(input ("Enter a number : "))
    computer = computer_choice(guess)
    
    
    while True: 
        human = take_user_input(guess)
        m_condition = conditions(human, computer)
    
        if conditions(human, computer):
         break 
    
#accepting user input
def take_user_input(guess):
    user_input = None
    while user_input not in guess :
        user_input = int(input ("choose a number : "))
    return user_input

def conditions(user_input, computer):
    if user_input > computer :
        print("choose lower")
        return False
    elif user_input < computer :
        print (" choose greater")
        return False
    else :
        print(" Nice guess ")
        return True
        
#capture the numbers
def computer_choice(guess):
    computer_choice = random.choice(guess)
    return computer_choice

main()