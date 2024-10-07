# https://leetcode.cn/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step=0
        for i in range(len(nums)-1):
            if nums[i]>step:
                step=nums[i]
            if step>0:
                step-=1
            else:
                return False
        return True
