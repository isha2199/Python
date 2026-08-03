'use strict' // remove it for non-strict mode

// this keyword in node with non-strict mode

console.log(this); // return {} empty object

function showThis(){
    console.log(this); // return global object
}
showThis();

let obj = {
    name: "John",
    f: function(){
        console.log(this);
        function g(){
            console.log(this); // return global object
        }
        g();
    }
}
obj.f(); // return object { name: 'John', f: [Function: f] }

function greet(){
    console.log(this.name);
}
const user = { name: "Isha" };
greet.call(user);
greet.apply(user);
const boundGreet = greet.bind(user);
boundGreet();
