# https://leetcode.cn/problems/compare-version-numbers/description/
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ls1=version1.split(".")
        ls2=version2.split(".")

        diff=abs(len(ls1)-len(ls2))
        if len(ls1)>len(ls2):
            ls2=ls2+[0]*diff
        elif len(ls1)<len(ls2):
            ls1=ls1+[0]*diff
        
        for a,b in zip(ls1,ls2):
            a=int(a)
            b=int(b)
            if a>b:
                return 1
            elif a<b:
                return -1
            
        return 0