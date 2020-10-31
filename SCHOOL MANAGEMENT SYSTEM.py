import pandas as pd
from teacher import teacher
from student import student
from subject import subject
try:
    n=0
    while (n!=4):
        print()
        print()
        print("----------------------------------------")
        print("SCHOOL MANAGEMENT SYSTEM")
        print("----------------------------------------")
        print("1. Admin Login")
        print("2. Teacher Login")
        print("3. Student Login")
        print()
        choice=int(input("Enter Your Choice : "))
        
        teachers=[]
        
        if(choice==1):
            print()
            print("----------------------------------------")
            print("Welcome Admin!")
            print("----------------------------------------")
            password=input("Password : ")

            if (password=="admin"):
                print()

                a=0
                while (a!=7):
                    print("----------------------------------------")
                    print("Welcome to Admin Panel")
                    print("----------------------------------------")
                    print("1. Add New Teacher")
                    print("2. Add New Student")
                    print("3. Add New Subject")
                    print("4. View Teachers")
                    print("5. View Students")
                    print("6. View Subjects")
                    print()

                    choice=int(input("Enter your Choice : "))

                    if (choice==1):
                        print()
                        t=teacher()
                        t.add_teacher()
                        print()
                        
                    elif (choice==2):
                         print()
                         s=student()
                         s.add_student()
                         print()
                        
                    elif (choice==3):
                        print()
                        sub=subject()
                        sub.add_subject()
                        print()

                    elif (choice==4):
                        print()
                        print("----------------------------------------")
                        t=teacher()
                        t.view_teacher()
                        print("----------------------------------------")
                        print()

                    elif (choice==5):
                        print()
                        print("----------------------------------------")
                        s=student()
                        s.view_student()
                        print("----------------------------------------")
                        print()
                        
                    elif (choice==6):
                        print()
                        print("----------------------------------------")
                        sub=subject()
                        sub.view_subject()
                        print("----------------------------------------")
                        print()
                        
                        
                    else:
                        print("Invalid Input")
                        print()
            else:
                print("Invalid password!")

        elif(choice==2):
            print()
            print("----------------------------------------")
            print("Welcome Teacher!")
            print("----------------------------------------")
            password=input("Password : ")

            if (password=="teacher"):
                print()

                a=0
                while (a!=7):
                    print("----------------------------------------")
                    print("Teacher's Portal")
                    print("----------------------------------------")
                    print("1. Add New Student")
                    print("2. Add New Subject")
                    print("3. View Students")
                    print("4. View Subjects")
                    print()

                    choice=int(input("Enter your Choice : "))

                    if (choice==1):
                        print()
                        s=student()
                        s.add_student()
                        print()

                    elif (choice==2):
                        print()
                        sub=subject()
                        sub.add_subject()
                        print()

                    elif (choice==3):
                        print()
                        print("----------------------------------------")
                        s=student()
                        s.view_student()
                        print("----------------------------------------")
                        print()
                        
                    elif (choice==4):
                        print()
                        print("----------------------------------------")
                        sub=subject()
                        sub.view_subject()
                        print("----------------------------------------")
                        print()

                    else:
                        print("Invalid Input")
                        print()
                        
            else:
                print("Invalid password!")

        elif(choice==3):
             print()
             data = pd.read_csv("E:\\coding\\python\\GTT MiniProject1\\student.csv")
             print("----------------------------------------")
             print("Welcome to Students Portal!")
             print("----------------------------------------")
             n=int(input("Enter your portal number : "))
             data.loc[n, :]
             print("----------------------------------------")
             print(data.loc[n , :])
             print("----------------------------------------")
    
        
        else:
            print()
            print("Invalid Input")

except KeyError as k:
    print("Invalid Key")

