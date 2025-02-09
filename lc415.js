/*
 * @lc app=leetcode.cn id=415 lang=javascript
 *
 * [415] 字符串相加
 * https://leetcode.cn/problems/add-strings/submissions/597894343/
 */

// @lc code=start
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    let idx=1;
    let res=""
    let flag=false;

    while(idx<=num1.length&&idx<=num2.length){
        a=+num1.at(-idx)
        b=+num2.at(-idx)

        c=a+b+flag
        if(c>=10){
            c-=10
            flag=true
        }else{
            flag=false
        }
        res=c+res
        idx++;
        console.log(c)
    }

    let num=null;
    if(idx<=num1.length){
        num=num1;
    }else if(idx<=num2.length){
        num=num2;
    }

    while(num&&idx<=num.length){
        a=+num.at(-idx)

        c=a+flag
        if(c>=10){
            c-=10
            flag=true
        }else{
            flag=false
        }
        res=c+res
        idx++;
    }
    if(flag){
        res=1+res
    }

    return res;
};
// @lc code=end

