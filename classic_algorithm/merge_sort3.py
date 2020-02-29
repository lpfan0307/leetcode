def merge(lst, l, mid, r):
    left = lst[:mid+1]
    right = lst[mid+1:r+1]
    k = 0
    while left and right:
        if left[0] < right[0]:
            lst[k] = left.pop(0)
        else:
            lst[k] = right.pop(0)
        k += 1
    tail = left if left else right
    for n in tail:
        lst[k] = n
        k += 1

def merge_sort(lst, l, r):
    if l < r:
        mid = (l + r - 1) //2
        merge_sort(lst, l, mid)
        merge_sort(lst, mid+1, r)
        merge(lst, l,mid, r)


arr = [1,4,6,8,2,5,6,9]
merge_sort(arr, 0, len(arr))

print(arr)
arr = arr[::-1]
merge_sort(arr, 0, len(arr))
print(arr)