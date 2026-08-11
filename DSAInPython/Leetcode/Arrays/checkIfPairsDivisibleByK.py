from ast import main
from typing import List
class checkPairsDivisibleByK:

    def canArrange(self, arr: List[int], k: int) -> bool:
        freq={}
        for n in arr:
            rem=n % k  # module operator gives +ve reminder only n python ( for -ve numbers as well) for no need of converting the negative rem to +ve like Java with condition as if rem < 0 => rem = rem + k
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
        freq= [0] * k
        for n in arr:
            rem = n % k
            freq[rem]=+1
        print(freq)
        # iterate till k/2 elements only
        for i in range(1,k//2):
            compliment = k - i
            if freq[compliment] != freq[i]:
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
