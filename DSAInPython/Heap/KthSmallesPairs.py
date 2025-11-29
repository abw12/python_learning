import heapq
from multiprocessing import heap
from typing import List

## nums1 = [1,7,11], nums2 = [2,4,6], k = 3
def k_Smallest_pairs(nums1:List[int],nums2:List[int],k:int) -> List[List[int]]:
    result=[]
    
    min_heap=[] # it will hold the tuple which 
    visited=set()
    heapq.heappush(min_heap,(nums1[0]+nums2[0],0,0))
    visited.add((0,0))

    while min_heap and len(result) < k:
        _, i, j = heapq.heappop(min_heap)
        result.append([nums1[i],nums2[j]]) # always adde the smalles pair in our final result
        
        #explore next neighbouring pair by moving right in nums1 array(ith index)
        if i+1 < len(nums1) and (i+1,j) not in visited:
            heapq.heappush(min_heap,(nums1[i+1],nums2[j],i+1,j))
            visited.add((i+1,j))
        
        ## explore next neighbouring pair by moving right in nums2 array(j index)
        if j+1 < len(nums2) and (i,j+1) not in visited:
            heapq.heappush(min_heap,(nums1[i]+nums2[j+1],i,j+1))
            visited.add((i,j+1))
    return result

def optimal_solution(nums1:List[int],nums2:List[int], k: int) -> List[List[int]]:

    min_heap=[]
    m=len(nums1)
    n=len(nums2)
    result=[]

    ## first only add the first column of the matrix formed mxn into pq
    for i in range(min(m,k)):
        heapq.heappush(min_heap,(i,0)) ## first column of the matrix

    while k > 0 and min_heap:
        top = heapq.heappop(min_heap)
        i=top[0]
        j=top[1]
        result.append([nums1[i],nums2[j]])
        if j+1 < n:
            heapq.heappush(min_heap,(i,j+1))
        k-=1
    return result



if __name__ == "__main__":
    nums1=[1,1,2]
    nums2=[1,2,3]
    k=3
    print(k_Smallest_pairs(nums1,nums2,k))
    print(optimal_solution(nums1,nums2,k))

