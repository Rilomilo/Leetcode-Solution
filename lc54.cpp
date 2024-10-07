// https://leetcode.cn/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150
#include <vector>
#include <iostream>

using namespace std;

struct point{
    int r=0;
    int c=0;
};

point next(point p, int d){
    if(d==0){
        p.c+=1;
    }else if(d==1){
        p.r+=1;
    }else if(d==2){
        p.c-=1;
    }else if(d==3){
        p.r-=1;
    }
    return p;
}

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int d=0;
        int m=matrix.size();
        int n=matrix[0].size();
        int total=m*n;
        int cnt=0;
        point p;
        vector<int> output=vector<int>();
        
        while(true){
            output.push_back(matrix[p.r][p.c]);
            matrix[p.r][p.c]=-101;
            cnt++;
            if(cnt==total) break;

            point next_p=next(p,d);
            if(next_p.r<0 || next_p.r>=m || next_p.c<0 || next_p.c>=n || matrix[next_p.r][next_p.c]==-101){
                d=(d+1)%4;
                p=next(p,d);
            }else{
                p=next_p;
            }
        }

        return output;
    }
};

int main(){
    vector<vector<int>> matrix ={{1,2,3,4},{5,6,7,8},{9,10,11,12}};
    Solution s=Solution();
    s.spiralOrder(matrix);
}