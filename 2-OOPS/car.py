class Car:
    def __init__(self,name,year,price):
        self.name=name
        self.year=year
        self.price=price
    
    def displayDetails(self):
        return f"{self.name},{self.price},{self.year}"
    

