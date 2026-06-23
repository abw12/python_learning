class Bikes:
    def __init__(self,name,year,price):
        self.name=name
        self.price=price
        self.year=year
    
    def displayDetails(self):
        return f"{self.name},{self.price},{self.year}"