/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let result=[]
    for(let i=0;i<arr.length;i+=size){
        let t=[]
        for(let j=0; j<size&&i+j<arr.length; j++){
            t.push(arr[i+j])
        }
        result.push(t)
    }

    return result
};