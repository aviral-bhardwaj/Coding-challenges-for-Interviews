class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ii,i in enumerate(nums):
            s=target-i
            for j in range(len(nums[ii+1:])):
                if nums[ii+1+j]==s:
                    return [ii,ii+j+1]