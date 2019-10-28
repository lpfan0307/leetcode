class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index = m + n -1
        idx1 = m -1
        idx2 = n -1
        while idx1>=0 and idx2>=0:
            v1 = nums1[idx1]
            v2 = nums2[idx2]
            if v2 > v1:
                nums1[index] = v2
                idx2 -= 1
            else:
                nums1[index] = v1
                idx1 -= 1
            index -= 1

        if idx1<0:
            while idx2 >= 0:
                nums1[index] = nums2[idx2]
                idx2 -= 1
                index -= 1


l1 = [4,5,6,0,0,0]
l2 = [1,2,3]
s = Solution()
s.merge(l1,3,l2,3)