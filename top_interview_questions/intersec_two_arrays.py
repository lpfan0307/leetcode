class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        result = []
        for num in count1:
            if num in count2:
                c = min(count1[num],count2[num])
                result = result + [num]*c
        return result
