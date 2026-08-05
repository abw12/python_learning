class productExceptSelfSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        #[1,2,3,4]
        # left calc = [1,1,2,6]
        # right calc = [24,12,8,6]
        # n = len(nums)
        # left = 1
        # for i in range(n):
        #     if i != 0:
        #         left = left * nums[i-1]
        #     result.append(left)        
        # right = 1
        # for i in range(n-1,-1,-1):
        #     if i != n-1:
        #         right = right * nums[i+1]
        #     result[i]*=right
        # return result

        prefix =1
        n = len(nums)
        result = [1] * n # preload the array size 
        for i in range(n):
            result[i]= prefix
            prefix*=nums[i]
        
        suffix=1
        for i in range(n-1,-1,-1):
            result[i]*=suffix
            suffix*=nums[i]
        return result