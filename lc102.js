/*
 * @lc app=leetcode.cn id=102 lang=javascript
 *
 * [102] 二叉树的层序遍历
 * https://leetcode.cn/problems/binary-tree-level-order-traversal/submissions/597952602/
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if(!root) return []
    let queue=[root]
    let result=[]
    
    while(queue.length!=0){
        let length=queue.length
        let layer=[]
        for(let i=0;i<length;i++){
            node=queue.shift()
            layer.push(node.val)
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)
        }
        result.push(layer)
    }

    return result;
};

// levelOrder([3,9,20,null,null,15,7])
// @lc code=end

