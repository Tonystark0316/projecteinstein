import random
def main():
    states = [ "rock" , "paper" , "scissors" ]
    user_ans=input('Enter your answer:\n')
    human=ans(user_ans, states)
    computer=comp_choice(states)
    print("You chose:", user_ans)
    print("Ai chose:", computer)

    if human == computer:
        print("It's a DRAW!")

    elif user_ans == "rock":
        if computer == "scissors":
            print("You WIN!")
        else:
            print("You lose!")

    elif user_ans == "paper":
        if computer == "rock":
            print("You WIN!")
        else:
            print("You lose!") 

    elif user_ans == "scissors":
        if computer == "paper":
            print("You WIN!")
        else:
            print("You lose!")

def ans(user_ans,states):
    while user_ans not in states:
        print('Invalid answer, enter either rock, paper or scissors')
        user_ans=input('Enter your answer:\n')
    return user_ans

def comp_choice(states):
    make_choice=random.choice(states)
    return make_choice

main()