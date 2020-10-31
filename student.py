import pandas as pd

class student:

    def add_student(self):
        print()
                    
        data = pd.read_csv("E:\\coding\\python\\GTT MiniProject1\\student.csv")
                    
        Sname=input("Enter Name : ")
        Sclass=input("Enter Class : ")
        Sdivision=input("Enter Division : ")
        Srn=input("Enter Roll Number : ")
        Spercentage=input("Enter Percentage : ")
        cols=["Name", "Class", "Division", "Roll Number", "Percentage"]

        new_row=[Sname, Sclass, Sdivision, Srn, Spercentage]
                    
        new_data=pd.DataFrame([new_row], columns=cols)
        data=pd.concat([data, new_data], sort=False)    

        data.to_csv("E:\\coding\\python\\GTT MiniProject1\\student.csv", index=False)
        print("Operation Successfull!")
        print()

    def view_student(self):
        data = pd.read_csv("E:\\coding\\python\\GTT MiniProject1\\student.csv")
        print(data)
