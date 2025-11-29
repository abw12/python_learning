from car import Car
from bikes import Bikes

def main():
    my_car = Car("Fortuner",2023 , "55Lac")
    my_bike = Bikes("Harley-Davidson", 2024, "17lac")

    print(my_car.displayDetails())  
    print(my_bike.displayDetails()) 

    
if __name__ == "__main__":
    main()