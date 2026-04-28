#project1
#School_portal_system
#takes_user_details_into_school_portal_system
from utils import Register_Student, save_student
def User_details():
    while True:
       print("\nWelcome to King's Academy")
       print("1.Register")
       print("2.Search for student")
       print("3.Pay fees")
       print("4.Exit")
       #taking_user's_choice
       Choice = input("Enter a Choice")
       if Choice =="1":
           print("Redirecting to Registration")
           Register_Student()
       elif Choice =="2":
           print("Enter student name to search")
       elif Choice == "3":
           print("Redirecting to payment portal")
       elif Choice =="4":
           print("thanks for visiting our school")
           break
       

User_details()
    
        

    




       
       
        

        
