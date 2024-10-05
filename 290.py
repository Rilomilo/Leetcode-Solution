# https://leetcode.cn/problems/word-pattern/submissions/570031863/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2s={}
        s2p={}

        words=s.split(" ")

        if len(pattern)!=len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] in p2s or words[i] in s2p:
                if words[i] not in s2p or pattern[i] not in p2s or p2s[pattern[i]]!=words[i] or s2p[words[i]]!=pattern[i]:
                    return False
            else:
                p2s[pattern[i]]=words[i]
                s2p[words[i]]=pattern[i]
        return True