def swap(tree, i, j):
    tmp = tree[i]
    tree[i] = tree[j]
    tree[j] = tmp

def headpify(tree, n, i):
    if i >= n-1:
        return
    max_idx = i
    left_node = 2*i + 1
    right_node = 2*i +2
    if left_node < n and  tree[left_node] > tree[max_idx]:
        max_idx = left_node
    if right_node < n and tree[right_node] > tree[max_idx]:
        max_idx = right_node
    if max_idx != i:
        swap(tree, max_idx, i)
        headpify(tree, n, max_idx)

arrs = [9,4,6,8,1,2,13,56,111]
arrs = arrs[::-1]
n = len(arrs)

last_node = int((len(arrs)-1)/2)
while last_node >= 0:
    headpify(arrs, n, last_node)
    last_node -= 1

while n > 0:
    swap(arrs, 0, n-1)
    n -= 1
    headpify(arrs, n, 0)

arr = [4,1,3,4,6,7,8,9,-1,0]
