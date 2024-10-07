// https://leetcode.cn/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n=matrix.size();
        int layer=n/2;

        for(int i=0;i<layer;i++){
            for(int j=0;j<n-2*i-1;j++){
                // printf("(%d,%d),(%d,%d),(%d,%d),(%d,%d)\n",i, i+j, i+j, n-1-i, n-1-i, n-1-i-j, n-1-i-j, i);
                // (i,i+j),(i+j,n-1-i),(n-1-i,n-1-i-j),(n-1-i-j,i)
                // 4-3, 3-2, 2-1
                swap(matrix[n-1-i-j][i], matrix[n-1-i][n-1-i-j]);
                swap(matrix[n-1-i][n-1-i-j], matrix[i+j][n-1-i]);
                swap(matrix[i+j][n-1-i], matrix[i][i+j]);
            }
        }
    }
};
