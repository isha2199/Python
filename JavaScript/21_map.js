const users = [
  { name: "Isha", age: 25 },
  { name: "Raj", age: 17 },
  { name: "Priya", age: 30 },
];

users.map((user) => console.log(user.name + " is " + user.age + " years old"));

Array.prototype.myMap = function (arr) {
  let newArr = [];
  for (let i = 0; i < arr.length; i++) {
    newArr.push(arr[i] * 2);
  }
  return newArr;
};
const nums = [1, 2, 3, 4];
console.log(nums.myMap(nums));

Array.prototype.myMapPolyfill = function (callback) {
  let newArr = [];
  for (let i = 0; i < this.length; i++) {
    newArr.push(callback(this[i]));
  }
  return newArr;
};
console.log(nums.myMapPolyfill((n) => n * 2));

const newArr = [];

const doubled = nums.reduce((acc, cur) => {
  // your logic here — build up 'acc' as a new array
  newArr.push(cur * 2);
  return (acc = newArr);
}, []);
console.log(doubled);

const evens = nums.reduce((acc, cur) => {
  // only push if cur is even
  if(cur % 2 == 0){
    acc.push(cur);
  }
  return acc;
}, []);
console.log(evens);

const nested = [
    [1, 2], 
    [3, 4], 
    [5, 6]
];
const flat = nested.reduce((acc, cur) => {
  // your logic here — result should be [1, 2, 3, 4, 5, 6]
  acc.push(...cur);
  return acc;
}, []);
console.log(flat);