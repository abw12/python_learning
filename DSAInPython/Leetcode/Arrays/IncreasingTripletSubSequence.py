from typing import List
class IncreasingTripletSubSequence:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf') # +ve infinity (equivalent of writting as INTEGER.MAX_VALUE in Java)
        second_smallest = float('inf')
        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= second_smallest:
                second_smallest = n
            else:
                return True
        return False