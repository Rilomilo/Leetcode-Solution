# https://leetcode.cn/problems/maximum-subarray/description/
# 每次向前看一个数字：如果累加和为正则继续，如果累加和为负则丢弃前面的

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=0
        r=0
        sum=nums[0]
        max_sum=sum

        while r<len(nums):
            if l==r:
                sum=nums[l]
            else:
                sum+=nums[r]
            r+=1
            
            max_sum=max(sum,max_sum)
            if sum<0:
                l=r

        return max_sum