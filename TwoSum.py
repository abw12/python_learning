def twoSum(nums: list[int], target: int) -> list[int]:
    map={}
    for i in range(len(nums)):
        if map.get(target - nums[i]) is not None:
            return [i,map[target - nums[i]]]
        map.update({nums[i]:i})
    return [-1,-1]

print(twoSum([2,7,11,15],9))