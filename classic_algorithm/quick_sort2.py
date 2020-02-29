def QuickSort(list, low, high):
    if high > low:
        k = Partitions(list, low, high)
        QuickSort(list, low, k-1)
        QuickSort(list, k+1, high)

def Partitions(list, low, high):
    left = low
    right = high
    k = list[low]
    while left < right:
        while list[right] > k and left< right:
            right -= 1
        while list[left]<=k and left<right:
            left += 1
        list[left], list[right] = list[right],list[left]
    list[low] = list[left]
    list[left] = k
    return left

array = [4,3,1,5,6,2,0]
QuickSort(array, 0, len(array)-1)
print(array)

array = [4,3,1,5,6,2,0]
array = array[::-1]
QuickSort(array, 0, len(array)-1)
print(array)