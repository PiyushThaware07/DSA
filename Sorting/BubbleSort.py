# Move the max element at the end of list by comparing.

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):  
        didSwap = False
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                didSwap = True
        if not didSwap:
            # print("Array Already Sorted")
            break
    print("Sorted Array:", arr)


array = [13,46,24,52,20,9]
array = [2,3,4,5,6]
array = [24 ,18 ,38 ,43 ,14 ,40 ,1 ,54]
print("Unsorted Array :",array )
sort(array)
