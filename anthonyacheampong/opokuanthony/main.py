
import csv

#take_user_input
def main():
    
    while True:
        print("WELCOME TO STAR LIGHT STUDENT PORTAL")
        print("Choose from 1 to 7 \n")
        print("choose 1 To Resgister \n")
        print("Choose 2 To make Enquiries \n")
        print("choose 3 To Search a Student \n")
        print("Choose 4 To make Update of Student info \n")
        print("Choose 5 To view student info \n")
        print("choose 6 To make Deletion \n")
        print("Choose 7 To Exit from this Portal \n ")
        choice = int(input("Enter your choice : "))
    
        #accepting user_input
        if choice == 1:
            name = input("Enter your name : ").upper()
            studentid = input ("Enter your student id : ")
            age = int(input("Enter your age : "))
            contact = input("Enter your phone number  : ")
            fees = int(input("Enter amount of fees paid : GHS "))
            city = input("Enter your city : ")
        
            print(f' congratulation {name} \n')
            print("Student successuflly registered \n")
        
            input("Press Enter to Exit : ")
    
            with open("student.txt", "a") as file:
                file.write(f" Name: {name}\n")
                file.write(f"Student id  {studentid}\n")
                file.write(f"Age  {age}\n")
                file.write(f"Contact {contact}\n")
                file.write(f"Fees {fees}\n")
                file.write(f"City {city}\n")
       
    
            with open("student.txt", "r") as file:
                print(file.read())
        
            with open("student.csv","a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, studentid, age, contact, fees, city])
            
      
    
    
        elif choice == 2:
            name = input("Enter your name please : ")
            print(f"Hello {name} \n")
            print("Welcome to Fact of Life Academy \n")
            print("Located at Sakora Woono in Kwabre Kumasi \n ")
            print("email: factoflife@yahoo.com \n")
            print("For more information contact us on : 0591476165")
         
         
        elif choice == 3:
            search = input("Enter student name or studentid to search : ")
            with open("student.csv","r") as file:
                reader = csv.reader(file)
            
                found = False
                for row in reader:
                
                    if search == row[0].capitalize() or search == row[1].capitalize() :
                        print("Student found\n")
                        print(f"Name: {row(0)}\n")
                        print(f"StudentId: {row(1)}\n")
                        print(f"Age: {row(3)}\n")
                        print(f"contact: {row(4)}\n")
                        print(f"Fees: {row(5)}\n")
                        print(f"City: {row(6)}\n")
                        found = True
                    
                    
                    if not found:
                        print("Student not found")
            
        elif choice == 4:
            name = input("Enter your name : ").upper()
            studentid = input ("Entter your student id : ")
            age = int(input("Enter your age : "))
            contact = input("Enter your phone number  : ")
            fees = int(input("Enter amount of fees paid : GHS "))
            city = input("Enter your city : ")
         
        
            with open("student.txt", "a") as file:
                file.write(f" Name: {name}\n")
                file.write(f"Student id  {studentid}\n")
                file.write(f"Age {age}\n")
                file.write(f"Contact {contact}\n")
                file.write(f"Fees  {fees}\n")
                file.write(f"City {city}\n")
        
    
            with open("student.txt", "a") as file:
                print(file.read())
            
            with open("student.csv","a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, studentid, age, contact, fees, city])
            
            print("Succeessfully Updated Student Info")
    
        elif choice == 5:
            with open("student.csv","a") as file:
                reader = csv.reader(file)
            
            for row in reader:
                print(row)

        elif choice == 6:
            delete_studentId = input(" Enter StudentId to delete : ")
            
            with open ("student.txt","r") as file:
                lines = file.readlines()
                new_file =[]
                delete = False
            
                for lines in lines :
                    
                    if f"Student_Id:{delete_studentId}" in lines:
                        delete = True 
                        continue
                    
                    #stop deleting after the seperator
                    if delete and "-----------------" in lines:
                        delete = False
                        continue
                    
                    if not delete:
                        new_file.append(lines)
                        
                        
                    with open("student.txt","w") as file:
                         file.writelines(new_file)
                          
                         
                print(" info succeessfully delete")
                print("sorry to see you go")
                   
        #EXITTING
        elif choice == 7:
            choice = input("Sure You Want to Exit ? Yes/ No : ").capitalize()
            if choice == "Yes" :
                print("Have A Nice Day")
                break
            elif choice == "No" :
                print (main)
                
        else :
            print("Invalid Input")
            
            
main()


input("Press Enter to Exit : \n ")