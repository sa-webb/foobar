const array1 = [1, 2, 4, 8];

const reducer = (accumulator, currentValue) => accumulator + currentValue;

console.log(array1.reduce(reducer)); // 15

console.log(array1.reduce(reducer, 5)); // 20 or 15 + 5 
