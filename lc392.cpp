// https://leetcode.cn/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        // 判断 s 是否为 t 的子序列。
        int si=0,ti=0;
        while(si<s.length()&&ti<t.length()){
            if(s[si]==t[ti]){
                si++;
            }
            ti++;
        }
        if(si==s.length()){
            return true;
        }else{
            return false;
        }
    }
};