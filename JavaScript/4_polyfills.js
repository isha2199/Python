// Map custom function
let myArr = [1,2,3,4,5];

let sqArr = myArr.map(function(x){
    return x*x;
});

console.log(sqArr); 

function myPolyfillMap(arr, callback){
    let newArr = [];
    for(let i=0 ; i<arr.length ; i++){
        newArr.push(callback(arr[i]));
    }
    return newArr;
}

function square(x){
    return x*x;
}

let mappedArr = myPolyfillMap(myArr, square);
console.log(mappedArr);

// filter custom function
let myArr2 = myArr.filter(function(x){
    return x%2 === 0;
})

function myPolyfillFilter(arr,callback){
    let newArr = [];

    for(let i=0;i<arr.length ; i++){
        if(callback(arr[i])){
            newArr.push(arr[i]);
        }
    }

    return newArr;
}

function checkEven(x){
    return x%2 === 0;
}

console.log( myPolyfillFilter(myArr, checkEven));

// reduce custom function

myArr3 = myArr.reduce(function(acc, curr){
    return acc + curr;
},0);

function myPolyfillReduce(arr, callback, initialValue){
    for(let i=0;i<arr.length;i++){
        initialValue = callback(initialValue, arr[i]);
    }
    return initialValue;
}

function sum(acc,curr){
    return acc + curr;
}

console.log(myPolyfillReduce(myArr, sum, 0));