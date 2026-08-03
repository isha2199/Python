// function getData(data, getNextData) {
//   setTimeout(() => {
//     console.log(data);
//     getNextData ? getNextData() : "";
//   }, 1000);
// }

// // callback hell problem
// getData(1, () => {
//   getData(2, () => {
//     getData(3);
//   });
// });

// const promise = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     resolve("done");
//   }, 1000);
// });

// promise.then((result) => {
//   console.log(result);
// });

// console.log("this runs first, immediately");

function asyncFunc() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("some data 1");
    }, 2000);
    resolve("success");
  });
}

function asyncFunc2() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("some data 2");
      resolve("success 2");
    }, 2000);
  });
}

console.log("fetching");
const p1 = asyncFunc();
p1.then((result) => {
  console.log(result);
});

const p2 = asyncFunc2();
p2.then((res) => {
  console.log(res);
});
