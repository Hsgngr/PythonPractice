"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 22:53 6.11.2020
LeetCode Day 6
https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3521/
"""


class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        high = max(nums) + 1
        low = 1
        return self.binary_search(nums, threshold, high, low)

    def binary_search(self, nums, threshold, high, low):

        if high == low:
            return high

        elif high -low ==1:
            low_total = self.find_total(nums,low)
            if low_total <= threshold:
                return low
            else:
                return high
        if high > low:
            mid = (high + low) // 2

        total = self.find_total(nums, mid)

        if total <= threshold:
            return self.binary_search(nums, threshold, mid, low)

        elif total > threshold:
            return self.binary_search(nums, threshold, high, mid)

    def find_total(self, nums, divisor):
        total = 0
        for num in nums:
            if num % divisor != 0:
                total += (num // divisor) + 1
            else:
                total += num // divisor

        return total


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    threshold = 6
    print(sol.smallestDivisor(nums, threshold))
'''
A better solution:

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        lo, hi = 1, max(nums)
        ans = -1
        
        while lo <= hi:
            mid = (lo+hi+1) / 2
            
            val = sum((num+mid-1)/mid for num in nums)
#            val = sum(-((-num)/mid) for num in nums)
            
            if val <= threshold: 
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
                
        return ans
'''