// https://leetcode.cn/problems/ransom-note/submissions/570017751/?envType=study-plan-v2&envId=top-interview-150
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()) return false;
        int sc[26]={0};

        for(int i=0;i<s.length();i++){
            sc[s[i]-97]++;
            sc[t[i]-97]--;
        }
        for(int i=0;i<26;i++){
            if(sc[i]!=0){
                return false;
            }
        }
        return true;
    }
};
