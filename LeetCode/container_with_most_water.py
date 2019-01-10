class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        ma=0
        for i in range(n):
            for j in range(i,n):
                m=min(height[i],height[j])
                if m*(j-i)>ma:
                    ma=m*(j-i)
        return ma

# Most Efficient Answer

class Solution(object):
    def maxArea(self, height):
        area = 0
        end = len(height) - 1
        max_number = max(height)
        start = 0
        while end > start and area < max_number * (end - start):
            area = max(area, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return area