// https://leetcode.cn/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
#include <vector>
#include <map>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> group = map<string, vector<string>>();
        vector<vector<string>> result = vector<vector<string>>();

        for(int i=0;i<strs.size();i++){
            string key = strs[i];
            sort(key.begin(),key.end());
            group[key].push_back(strs[i]);
        }
                
        for(auto& pair:group){
            result.push_back(pair.second);
        }

        return result;
    }
};