# It is all about finding the minimum and swap
# Complexity : O(n2)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:         # swap element at the outer loop so that it takes less time.
            swap(arr, i, min_index)
        print(arr)
    print("Sorted Array:", arr)
array = [13,46,24,52,20,9]
print("Unsorted Array :",array )
sort(array)
