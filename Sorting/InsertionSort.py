# Select an element from unsorted array and placed it into the sorted array.

def sort(arr):
    size = len(arr)
    for i in range(1,size):
        temp = arr[i]
        previous = i-1
        while (previous>=0 and arr[previous]>temp):
            arr[previous+1] = arr[previous]
            previous = previous-1
        arr[previous+1] = temp
    print("Sorted Array : ",arr)
        

array = [13,46,24,52,20,9]
print("Unsorted Array :",array )
sort(array)
