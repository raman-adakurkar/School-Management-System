import pandas as pd

class subject:

    def add_subject(self):
        print()
                    
        data = pd.read_csv("E:\\coding\\python\\GTT MiniProject1\\subject.csv")
                    
        Subname=input("Enter New Subject : ")
        cols=["Subject Name"]

        new_row=[Subname]
                    
        new_data=pd.DataFrame([new_row], columns=cols)
        data=pd.concat([data, new_data], sort=False)    

        data.to_csv("E:\\coding\\python\\GTT MiniProject1\\subject.csv", index=False)
        print("Operation Successfull!")
        print()

    def view_subject(self):
        data = pd.read_csv("E:\\coding\\python\\GTT MiniProject1\\subject.csv")
        print(data)


