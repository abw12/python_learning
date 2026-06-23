class Employee:


#   ## default Constructor
#     def __init__(self):  ## If we don't define the default constructor than it will be added at runtime by python interpreter 
#         pass  
    ## NOTE : python does not support multiple built-in constructor so if we want to pass the parametrized construction function 
    ## __init__ then object is always created using this constructor function only  
  
  ## Parameterized Constructor 
    def __init__(self,name,age,salary): ## self is like 'this' keyword in java, pointing the reference to this instance of the class 
        self.name =name
        self.age =age
        self.salary = salary
        print("Add Details of new Employee...")


# e1 = Employee() ## will not work since the __init__ function defined most recently is invoked by interpreter when an object is created and here its an parametrized function
e2 = Employee("Abhishek",26,"25 LPA")
print(e2.name,e2.age,e2.salary)


