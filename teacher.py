import pandas as pd

class teacher:

    def add_teacher(self):
        print()
                    
        data = pd.read_csv("E:\\coding\\python\\GTT MiniProject1\\teacher.csv")
                    
        Tname=input("Enter Name : ")
        Sname=input("Enter Subject : ")
        Salary=input("Enter Salary : ")
        cols=["Name", "Subject", "Salary"]

        new_row=[Tname, Sname, Salary]
                    
        new_data=pd.DataFrame([new_row], columns=cols)
        data=pd.concat([data, new_data], sort=False)    

        data.to_csv("E:\\coding\\python\\GTT MiniProject1\\teacher.csv", index=False)
        print("Operation Successfull!")
        print()

    def view_teacher(self):
        data = pd.read_csv("E:\\coding\\python\\GTT MiniProject1\\teacher.csv")
        print(data)


