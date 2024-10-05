// https://leetcode.cn/problems/ransom-note/submissions/570017751/?envType=study-plan-v2&envId=top-interview-150
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> rc=vector<int>(26);
        vector<int> mc=vector<int>(26);

        for(int i=0;i<ransomNote.length();i++){
            rc[ransomNote[i]-97]++;
        }
        for(int i=0;i<magazine.length();i++){
            mc[magazine[i]-97]++;
        }
        for(int i=0;i<26;i++){
            if(rc[i]>mc[i]){
                return false;
            }
        }
        return true;
    }
};