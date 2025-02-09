// https://leetcode.cn/problems/return-length-of-arguments-passed/submissions/598012038/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */