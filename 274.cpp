// https://leetcode.cn/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int hIndex(std::vector<int>& citations) {
        int i;
        sort(citations.begin(), citations.end(), greater<int>());
        for(i=0;i<citations.size();i++){
            if(citations[i]<i+1) break;
        }
        return i;
    }
};
