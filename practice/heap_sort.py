def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
def heapify(array, i, n):
    if i >= n-1 :
        return 
    left = 2 * i + 1
    right = 2 * i + 2
    max_i = i
    if left < n and array[left] > array[max_i]:
        max_i = left
    if right < n and array[right] > array[max_i]:
        max_i = right 
    if max_i != i:
        swap(array, max_i, i)
        heapify(array, max_i, n)
array = [9,4,6,8,1,2,13,56,111]
array = array[::-1]
last_not_left_node = (len(array) - 1) // 2
n = len(array)
while last_not_left_node >= 0:
    heapify(array, last_not_left_node, n)
    last_not_left_node -= 1

while n > 0:
    swap(array, 0, n-1)
    n -= 1
    heapify(array, 0, n)
print(array)