class Employees():
    def __init__(self,FirstName,LastName,Age):
        self.FirstName=FirstName
        self.LastName=LastName
        self.Age=Age
        

class DataScience(Employees):
    def __init__(self):
        self.Programming=[]

class Marketing(Employees):
    def __init__(self):
        self.SoftSkill=[]
        
Semih= Employees("Semih", "Çetin", 21)
Semih= DataScience()
Semih.Programming.append("SQl")
print(Semih.Programming)
