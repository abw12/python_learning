from ast import main
from typing import List
class checkPairsDivisibleByK:

    def canArrange(self, arr: List[int], k: int) -> bool:
        freq={}
        for n in arr:
            rem=n % k  # module operator gives +ve reminder only in python ( for -ve numbers as well) so no need of converting the negative rem to +ve like Java with condition as if rem < 0 => rem = rem + k
            freq[rem] = freq.get(rem,0)+1
        print(freq)

        for rem,count in freq.items():
            if rem == 0:
                if count % 2 != 0:
                    return False
            else:
                compliment = k - rem
                if freq[rem] != freq.get(compliment,0):
                    return False
        return True

    def usingKSizeArray(self, arr:List[int], k :int) -> bool:
        # create a k-size array , array index will define remainder of each element and array index value will define the count of that remainder
        freq=[0]*k
        for n in arr:
            rem = ((n % k) + k) % k # This is safer approach for -ve numbers although we could directly use the n % k like above in python since Python's modulo operator handles negatives correctly (e.g., -1 % 5 = 4)
            freq[rem]+=1
        print(freq)
        # Case 1: Remainder 0 elements must pair among themselves
        if freq[0] % 2 != 0:
            return False 
        # Case 2: For each remainder i, check its complement k - i
        for i in range(1,(k//2)+1): # doing +1 since range method end index is excluding 
            if i == k-i:
                # When k is even and i == k / 2, they must pair with each other (eg k=6; i= k //2 => 3 and current index i is also 3.so below else conditio if freq[3] != freq[3]:  # Always evaluates to False! thats why we need this if condition)
                if freq[i] % 2 != 0:
                    return False
            else:
                if freq[i] != freq[k-i]:
                    return False
        return True
                
        



def main():
    arr = [1,2,3,4,5,10,6,7,8,9]
    # arr = [1,2,3,4,5,6]
    k = 5
    obj = checkPairsDivisibleByK()
    print(obj.canArrange(arr,k))
    print(obj.usingKSizeArray(arr,k))

if __name__ == "__main__":
    main()
