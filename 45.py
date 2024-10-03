# https://leetcode.cn/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def jump(self, nums: List[int]) -> int:
        count=[len(nums)]*len(nums)
        count[0]=0

        for i in range(len(nums)):
            span=nums[i]
            for j in range(1,span+1):
                if i+j<len(nums) and count[i]+1<count[i+j]:
                    count[i+j]=count[i]+1
        return count[-1]
