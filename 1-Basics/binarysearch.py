## [1,2,3,4,5,6] sorted space

## implement the binary search to find the 4 from the above list

def findNumber(input:list,target:int):
    left = 0
    right = len(input) - 1
    while left <= right :
        mid = left + (right-left) // 2 ##  the // operator is used for floor division. This means it divides two numbers and rounds the result down to the nearest whole number
        if(input[mid] == target):
            return mid
        elif(input[mid] < target):
            left = mid+1   
        else:
            right = mid-1
    
    return -1

input = [1,2,3,4,5,6]
print(findNumber(input,5))

if __name__ == "__main__":
    findNumber([1,2,6,8,9],2)