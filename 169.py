# https://leetcode.cn/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        max_item = max(d.items(), key=lambda x: x[1])
        return max_item[0]