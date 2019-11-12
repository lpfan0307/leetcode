
class Solution:
    def maxArea(self, height):
        left, right, maxarea = 0, len(height)-1, 0  # 初始化双指针
        while left < right:
            if height[left] < height[right]:  # 从左向右移动
                tmp = height[left]*(right-left)
                left += 1
            else:
                tmp = height[right] * (right - left)  # 从右向左移动
                right -= 1
            maxarea = tmp if maxarea < tmp else maxarea  # 更新最大容量
        return maxarea
