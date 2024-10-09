#include <vector>
#include <iostream>
#include <queue>

using namespace std;

// // 319 / 323 个通过的测试用例
// class Solution {
// public:
//     int trap(vector<int>& height) {
//         int h_max=0;
//         int count=0;
//         for(int i=0;i<height.size();i++){
//             if(height[i]>h_max) h_max=height[i];
//         }
//         for(int h=1;h<=h_max;h++){
//             int r=-1;
//             for(int i=0;i<height.size();i++){
//                 if(height[i]>=h){
//                     if(r!=-1){
//                         count+=i-r-1;
//                     }
//                     r=i;
//                 }
//             }
//         }
//         return count;
//     }
// };


class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> fill=vector<int>(height.size());

        int count=0;
        int max=0;
        for(int i=0;i<height.size();i++){
            if(height[i]>max){
                max=height[i];
            }
            fill[i]=max;
        }
        max=0;
        for(int i=height.size()-1;i>=0;i--){
            if(height[i]>max){
                max=height[i];
            }
            fill[i]=min(fill[i],max);
        }

        for(int i=0;i<fill.size();i++){
            count+=fill[i]-height[i];
        }
        return count;
    }
};
