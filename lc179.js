// https://leetcode.cn/problems/largest-number/submissions/597872939/

/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    nums=nums.map(v=>String(v))
    nums.sort(function(a,b){
        return a+b>b+a?-1:1
    })
    while(nums.length>1 && nums[0]=="0"){
        nums.shift()
    }

    return nums.join("")
};