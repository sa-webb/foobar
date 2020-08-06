/**
 * @url https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find
 * @tutorial Find an object in an array by one of its properties
 */

const inventory = [
  { name: "apples", quantity: 2 },
  { name: "bananas", quantity: 0 },
  { name: "cherries", quantity: 5 },
];

function isCherries(fruit) {
  return fruit.name === "cherries";
}

// Using arrow functions and destructuring
const result = inventory.find(({ name }) => name === "apples");
const resultIndex = inventory.findIndex(({ name }) => name === "apples");

console.log(inventory.find(isCherries)); // { name: 'cherries', quantity: 5 }
console.log(inventory.findIndex(isCherries)); // 2

console.log(result); // { name: 'apples', quantity: 2 }
console.log(resultIndex); // 0
