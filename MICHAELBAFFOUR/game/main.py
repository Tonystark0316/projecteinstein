import random
def main():
    state = ['rock','paper','scissors']
    user_input = ("Enter a valid input from the list : ")
    human = take_userinput(user_input,state)
    computer = make_computer_choice(state)
    result = checking_result(human,computer)
    print(result)

def take_userinput(user_input,state):
    #pass
    #rock, paper or scissors
    while user_input not in state:
        user_input = input("Choose one of the items(rock," \
        "paper, scissors) : ")
    return user_input

def make_computer_choice(state):
    computer_choice = random.choice(state)
    return computer_choice


#checking result
def checking_result(human,computer):
    if human == 'rock' and computer == 'scissors':
        return "You won"
    elif human == 'rock' and computer == 'paper':
        return'computer won'
    elif human =='rock' and computer == 'rock':
        return 'Its a tie'
    elif human == 'scissors' and computer == 'rock':
        return 'Computer won'
    elif human == 'scissors' and computer == 'paper':
        return 'You won'
    elif human == 'scissors' and computer == 'scissors':
        return 'Its a tie'
    elif human == 'paper' and computer == 'rock':
        return 'You won'
    elif human =='paper' and computer == 'scissors':
        return 'Computer won'
    elif human == 'paper' and computer == 'paper':
        return 'Its a tie'
    else:
        return 'Error'
    
main()
