// https://leetcode.cn/problems/isomorphic-strings/submissions/570023169/?envType=study-plan-v2&envId=top-interview-150
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        vector<short> mapper=vector<short>(128, -999);
        vector<bool> f=vector<bool>(128);

        for(int i=0;i<s.length();i++){
            if(mapper[s[i]]==-999 && f[t[i]]==false){
                mapper[s[i]]=s[i]-t[i];
                f[t[i]]=true;
            }else if(mapper[s[i]]!=s[i]-t[i]){
                return false;
            }
        }
        return true;
    }
};