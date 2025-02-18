// https://leetcode.cn/problems/is-object-empty/description/?envType=study-plan-v2&envId=30-days-of-javascript
/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    let keys=Object.keys(obj)
    return !keys.length
};