def heapify(arr,n,i):
    largest=i # largest is representing the parent node
    left=2*i+1
    right=2*i+2

    # compare with the left child
    if left < n and arr[left] > arr[largest]:
        largest=left
    # compare with the right child
    if right < n and arr[right] > arr[largest]:
        largest=right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)


def build_max_heap(arr):
    n = len(arr)
    #start from the last parent node
    # ( the last non-leaf node in complete binary tree represented as an array is at index n //2 -1)
    for i in range(n // 2-1, -1, -1): ## so find the middle +1 index in the given array and iterate till the 0th index
            heapify(arr,n,i)
    return arr

if __name__ == "__main__":
    arr=[3,2,1,5,6,4]
    print(build_max_heap(arr))


        # after 1st iteration arr will look like
        # [3,6,1,5,2,4]
        # 2nd
        # [6,3,1,5,2,4]
        # 3rd
        #[6,5,1,3,2,4]
