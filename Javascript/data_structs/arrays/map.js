/**
 * @method map creates a new array with the results of calling a provided function
 * on every element in the calling array.
 * @method forEach executes a provided function once for each array element
 * 
 * map is up to 70% faster than forEach and allows method chaining
 */

const array1 = [1, 2, 4, 8];

console.log(array1.map((x) => x));
// [ 1, 2, 4, 8 ]

array1.forEach(x => console.log(x))
/* 
1
2
4
8
*/