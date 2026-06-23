# # print("Hello world")

# ## different data type in python ####

# # Numeric type
# ## Int
# # a =1
# # print(a)

# # ## float
# # b = 1.5
# # print(b)

# # ## complex
# # c = complex('2j')  ## there are two parameters 1st real part and 2nd imaginary part
# # print(c)



# # marks = {}
# # sub1= input("Enter the 1st subject name: ")
# # marks[sub1] = int(input("Enter the marks: "))
# # sub2 = input("Enter the 2nd subject name: ")
# # marks[sub2] = float(input("Enter the marks: "))
# # sub3=input("Enter the 3rd subject name: ")
# # marks[sub3] = int(input("Enter the marks: "))

# # print(marks)

# # print("abhishek","wasave") ## by default sep is space 
# # print("abhishek",end=" ") ## to print sentances on same line by default end="\n" hence next print statement is printed on next line
# # print("wasave")


# ## WAF to check if a number is prime or not ##

# def prime_num_check(n):
#     if(n < 2):
#         print("Not a Prime")
#     for i in range(2,n):
#         if(n % i == 0):
#             print("Not a Prime")
#             break
#     else:
#         print("Is Prime")     

# prime_num_check(15)

# ## fibonacci series using recursion ## 

# ## 0 1 1 2 3 5 8 13 21

# def fibbo(n):
#     ## base condition 
#     if(n < 2):
#         return 1 
#     return fibbo(n - 2) + fibbo(n -1)

# print("Fibbonacci series value = ", fibbo(7))


# ## WAF to calculte the sum of first n natural numbers 

# def calc_sum(n):
#     if(n == 0):
#         return 0 
#     return calc_sum(n-1) + n

# print(calc_sum(10))

# ## WAF to  print all elements in a list

# num_list = [1,2,3,4,5,6,7,8]

# def calc_printEl(nums,idx):
#     ## base condition
#     if(idx == len(nums)):
#         return
#     print(nums[idx])
#     calc_printEl(nums,idx +1)

# calc_printEl(num_list,0)


from ast import Not


contact_details={
    "name": "Abhishek Wasave",
    "phnNumber":  8459319614,
    "pinCode" : 401303,
    "city": "Virar"
}


# def fetchContactDetails():
#     try:
#         return contact_details['age']
#     except:
#         raise Exception("Key does not Exist in contact_details")

# print(fetchContactDetails())


### Leetcode question

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
# Return the highest altitude of a point.
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

def highestAltitude(gain:list[int]) -> int:
    highest=0
    sum=0
    for i in range(len(gain)):
        sum+=gain[i]
        if highest < sum:
            highest=sum
    return highest

# In Python, variables do not store values directly.
# Variables store references to objects.
a = [1,2,3,4]
b=a # b point to same reference as 'a' (same list object) 
print(a)
print(b)
b.append(10)
print(a)
print(b)

# Reassingment concept

x=10
x=20 
# Here, x first points to 10, then points to 20.
# You did not modify 10.
# You changed what x points to.

## Mutation
x=[10,20,30]
x.append(40)
# Here, the same list object is modified.
# The variable still points to the same object, but the object’s internal value changed.
