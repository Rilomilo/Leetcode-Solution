// https://leetcode.cn/problems/allow-one-function-call/submissions/598014974/?envType=study-plan-v2&envId=30-days-of-javascript
/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let flag=false
    
    return function(...args){
        if(!flag){
            flag=true
            return fn(...args)
        }else{
            return undefined
        }
    }
};

fn = (a,b,c) => (a + b + c)
const onceFn = once(fn);
console.log(onceFn(1, 2, 3)) // 6
console.log(onceFn(2, 3, 6));
 // undefined, fn 没有被调用
/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */