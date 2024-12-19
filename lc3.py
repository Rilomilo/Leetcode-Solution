# https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        r=1
        length=1
        chars=set()
        chars.add(s[0])

        while r<len(s):
            if s[r] not in chars:
                chars.add(s[r])
                length=max(length, r+1-l)
                r+=1
            else:
                chars.remove(s[l])
                l+=1

        return length