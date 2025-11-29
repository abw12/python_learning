## 10 List comprehension example

# list=[x for x in  q(10)]  
squares =[x**2 for x in range(10)] ## square root of each number in the range 0-9
## above line is equivalent to 
# list2=[]
# for x in range(10):
#     list2.append(x)

print(f'basic list comprehension example: {list}')
# print(list2)
print(f'square root of numbers {squares}')

## get all the even numbers from the list
evens=[]
for i in range(50):
    if i % 2 == 0:
          evens.append(i)
print(f'Evens: {evens}')

## somthing using list comprehension
evensList = [i for i in range(50) if i % 2 == 0] ## you can put the if condition check after the for loop within the list
print(f'Even list comprehension {evensList}')

## The condition after 'for' acts like a filter (similar to a filter() call).
oddlist = [i for i in range(10) if i%2!=0] 

## The condition before 'for' acts like a ternary expression (similar to a map() transformation).
oddlist = [i if i%2!=0 else None for i in range(10)] 

## return string which 1st character is 'a' and last character is 'y'

input_string=['any','albany','nothing','sock','tony','','ay']
result=[]
for string in input_string:
     if len(string) <=1:
          continue
     if string[0] != 'a':
          continue
     if string[-1] != 'y':
          continue
     result.append(string)
print(f'valid string: {result}')

## using list comprehension
## NOTE here the conditions are opposite of the above code. Just a way of writing in list comprehension
## list comprehension can span out in multiple lines 
valid_string=[
     string
     for string in input_string
     if len(string) >=2
     if string[0] == 'a'
     if string[-1] == 'y'
]
print(f'valid string list: {valid_string}')
## NOTE whenever there is if condition on the right hand side of the for loop in list comprehension it means we are filtering the value.


## Flatenning a matrix ( example of nested for loops in list comprehension)
matrix= [[1,2,3],[4,5,6],[7,8,9]]
flattened_list=[]
for row in matrix:
     for num in row:
          flattened_list.append(num)
print(f'Flattened list : {flattened_list}')

flattened_list_comp =[num for row in matrix for num in row]  ## nested for loops
print(f'Flattened list comp : {flattened_list_comp}')

## categories number as even and odd 
categories = []

for num in range (10):
    if num % 2 == 0:
        categories.append("Even")
    else:
         categories.append("Odd")
print(f'categories even and odd : {categories}')

## NOTE whenever there is if condition on the left hand side of the for loop in list comprehension we are placing the value on basis of the if condition in the list.

categories_comp = [
     "Even" if num % 2 == 0 else "Odd"
     for num in range(10)
]
print(f'categories by comp {categories_comp}')


## List comp with function

def square(x):
     return x**2
func_square_list = [square(x) for x in range(10)] ## we can use the function call within the list comprehension even for if conditions as well.
print(f'function list comprehension: {func_square_list}')


## creating a dictionary using list comprehension

pairs = [("a",1),("b",2),("c",3)] ## list of tuples 

my_dict= {k:v for k,v in pairs} ## these will iterate on each tuple within the list and map the key and value in the dictionary
my_dict_squared = {k:square(v) for k,v in pairs} ## can apply any function call as well
print(f'dict {my_dict}')
print(f'square dict {my_dict_squared}')

## removing duplicates from the list ( creating set using list comprehension)

nums = [1,2,2,3,3,3,4,4,4,4]
my_set = {x**2 for x in nums} ## if we don't pass key and value both then python understand that its a set and not a dictionary
print(f'set comp {my_set}')
