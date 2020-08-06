/**
 * @url https://www.educative.io/blog/data-structures-arrays-javascript-tutorial
 * @tutorial ArrayOps on simple arrays
 * @var nums array of integers
 * @method push(val) appends new element to the end of the array.
 * @method pop() removes the last element from the array.
 * @method shift() removes the first element of the array.
 * @method unshift(...vals) pushes new elements onto the front of the array.
 * @method splice(insert_index,remove_index_range,new_element)
 * @method length returns the length of the array
 * @method toString() returns a string value of the array
 * @method reverse() returns the reversed array
 */

var numbers = [67, 12, 76, 28, 7]

console.log(numbers)
// [ 67, 12, 76, 28, 7 ]

numbers.push(8)
console.log(numbers)
// [ 67, 12, 76, 28, 7, 8 ]

numbers.pop()
console.log(numbers)
// [ 67, 12, 76, 28, 7 ]

numbers.shift()
console.log(numbers)
// [ 12, 76, 28, 7 ]

numbers.unshift(1,2)
console.log(numbers)
// [ 1, 2, 12, 76, 28, 7 ]

console.log(numbers.length)
// 6

console.log(numbers.toString())
// 1,2,12,76,28,7

console.log(numbers.reverse())
// [ 7, 28, 76, 12, 2, 1 ]
