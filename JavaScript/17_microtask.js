// console.log("a");

// setTimeout(() => {
//   console.log("c");
// }, 1);

// Promise.resolve()
//   .then(() => console.log("d"))
//   .then(() => console.log("e"));

// console.log("b");


console.log("start");

setTimeout(()=>{
    console.log("time out 1");
    Promise.resolve().then(()=> console.log("promise inside timeout"));
},0);

setTimeout(()=>{},0);

Promise.resolve().then(()=> console.log("promise 1"));
console.log("end");