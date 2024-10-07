# https://leetcode.cn/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            while True:
                nums.remove(val)
        except ValueError:
            pass
        return len(nums)