def merge(arr_left, arr_right):
    left_num = len(arr_left)
    right_num = len(arr_right)
    res = []
    i,j,k = 0,0,0
    while i < left_num and j < right_num:
        if arr_left[i] < arr_right[j]:
            res.append(arr_left[i])
            i += 1
        else:
            res.append(arr_right[j])
            j += 1
    if i < left_num:
        res += arr_left[i:]
    else:
        res += arr_right[j:]
    return res

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
arr = [1,4,6,8,2,5,6,9]
res = merge_sort(arr)
print(res)

print(arr)
arr = arr[::-1]
res = merge_sort(arr)
print(res)