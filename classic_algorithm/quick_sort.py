def quick_sort(array, left, right):
    if left >= right:
        return 
    low = left
    high = right 
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        while left < right and array[left] <= key:
            left += 1
        tmp = array[left]
        array[left] = array[right]
        array[right] = tmp
    key = array[low]
    array[low] = array[left]
    array[left] = key
    quick_sort(array, low, left -1)
    quick_sort(array, left+1, high)

array = [4,3,1,5,6,2,0]
quick_sort(array, 0, len(array)-1)
print(array)

# array = [4,3,1,5,6,2,0]
# array = array[::-1]
# quick_sort(array, 0, len(array)-1)
# print(array)