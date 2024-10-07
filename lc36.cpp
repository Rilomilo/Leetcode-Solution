// https://leetcode.cn/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
#include <vector>
#include <iostream>

using namespace std;

vector<vector<char>> board = {
    {'5','3','.','.','7','.','.','.','.'},
    {'6','.','.','1','9','5','.','.','.'},
    {'.','9','8','.','.','.','.','6','.'},
    {'8','.','.','.','6','.','.','.','3'},
    {'4','.','.','8','.','3','.','.','1'},
    {'7','.','.','.','2','.','.','.','6'},
    {'.','6','.','.','.','.','2','8','.'},
    {'.','.','.','4','1','9','.','.','5'},
    {'.','.','.','.','8','.','.','7','9'}
};



class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        short row[9]={};
        short col[9]={};
        short block[9]={};

        for(int r=0; r<9;r++){
            for(int c=0;c<9;c++){
                if(board[r][c]!='.'){
                    short d=board[r][c]-48;
                    short bit=1<<(d-1);
                    if(row[r]&bit) return false;
                    else row[r]|=bit;
                    if(col[c]&bit) return false;
                    else col[c]|=bit;
                    int b=r/3*3+c/3;
                    if(block[b]&bit) return false;
                    else block[b]|=bit;
                }
            }
        }
        return true;
    }
};

int main(){
    Solution s= Solution();
    s.isValidSudoku(board);
    return 0;
}