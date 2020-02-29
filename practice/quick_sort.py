def quick_sort(array, left, right):
    if left >= right:
        return 
    low = left
    high = right
    key = array[low]
    while left < right :
        while left < right and array[right] > key:
            right -= 1
        while left < right and array[left] <= key:
            left += 1
        tmp = array[left]
        array[left] = array[right]
        array[right] = tmp
    array[low] = array[left]
    array[left] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)