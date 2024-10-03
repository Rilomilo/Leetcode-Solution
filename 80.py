# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag=0
        pointer=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                flag+=1
                if flag>=2:
                    continue
            else:
                flag=0
            nums[pointer]=nums[i]
            pointer+=1
        return pointer