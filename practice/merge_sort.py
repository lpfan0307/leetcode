def merge(left, right):
    res = []
    while left and right :
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res = res + left + right
    return res

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

arr = [1,4,6,8,2,5,6,9]
res = merge_sort(arr)
print(res)

print(arr)
arr = arr[::-1]
res = merge_sort(arr)
print(res)