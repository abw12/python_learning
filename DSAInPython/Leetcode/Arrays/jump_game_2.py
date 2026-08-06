from typing import List
class jumpGame2:
    def soultion(self,nums:List[int]) -> int:
        near=far=jump=farthest=0
        n = len(nums)
        while far < n-1: # This will break out of loop once we reach the last index which is guranteed in the question
            for i in range (near,far+1):
                curr_jump = i + nums[i]
                if farthest < curr_jump: # these two ines can be replaced by using the built-in max function
                    farthest = curr_jump
            near=far+1
            far=farthest
            jump+=1
        return jump
    