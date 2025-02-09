// https://leetcode.cn/problems/array-reduce-transformation/submissions/598009446/?envType=study-plan-v2&envId=30-days-of-javascript
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let v=init;
    for(let i=0;i<nums.length;i++){
        v=fn(v, nums[i])
    }
    return v;
};