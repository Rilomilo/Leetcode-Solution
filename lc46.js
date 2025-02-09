/*
 * @lc app=leetcode.cn id=46 lang=javascript
 *
 * [46] 全排列
 * https://leetcode.cn/problems/permutations/submissions/597934807/
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */

var permute = function(nums) {
    let result=[]

    function fun(cur, left){
        if(left.length==0){
            result.push(cur)
            return
        }
        for(let i=0;i<left.length;i++){
            let cur1=cur.slice()
            let left1=left.slice()

            let n=left1.splice(i,1)[0]
            cur1.push(n)

            fun(cur1, left1)
        }
    }
    fun([], nums)

    return result
};
// @lc code=end

