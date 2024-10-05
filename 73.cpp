// https://leetcode.cn/problems/set-matrix-zeroes/submissions/570007369/?envType=study-plan-v2&envId=top-interview-150
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int rs=matrix.size();
        int cs=matrix[0].size();
        bool *rf=(bool*)calloc(rs, sizeof(bool));
        bool *cf=(bool*)calloc(cs, sizeof(bool));

        for(int r=0;r<rs;r++){
            for(int c=0;c<cs;c++){
                if(matrix[r][c]==0){
                    rf[r]=1;
                    cf[c]=1;
                }
            }
        }
        for(int i=0;i<rs;i++){
            if(rf[i]){
                for(int c=0;c<cs;c++){
                    matrix[i][c]=0;
                }
            }
        }
        for(int i=0;i<cs;i++){
            if(cf[i]){
                for(int r=0;r<rs;r++){
                    matrix[r][i]=0;
                }
            }
        }
    }
};