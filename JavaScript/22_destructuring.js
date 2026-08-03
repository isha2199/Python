const user = { profile: { age: 0 } };
const age = user?.profile?.age ?? 18;
console.log(age);

const words = ["apple", "banana", "apple", "cherry", "banana", "apple"];
// O/p: { apple: 3, banana: 2, cherry: 1 }

const count = words.reduce((acc, curr) => {
  acc[curr] = (acc[curr] || 0) + 1;
  return acc;
}, {});
console.log(count);

function flattenDeep(arr) {
  return arr.reduce((acc, curr) => {
    if (Array.isArray(curr)) {
      acc.push(...flattenDeep(curr));
    } else acc.push(curr);

    return acc;
  }, []);
}

console.log(flattenDeep([1, [2, 3], [4, [5, 6, [7, 8]]]]));

const obj = {
  a:1,
  b:{
    c: 2,
    d:{
      e: 3
    }
  }
};

function flattenDeepObj(obj, parentKey='', result={}){

  for(let key in obj){
    const newKey = parentKey ? `${parentKey}.${key}` : key;
    if(typeof obj[key] === 'object' && obj[key] !== null){
      flattenDeepObj(obj[key], newKey, result);
    } else{
      result[newKey] = obj[key];
    }
  }

  return result;
}

console.log(flattenDeepObj(obj));

