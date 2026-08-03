function sayHello(){
    console.log("hellow");

}

sayHello();

let a = [1, 2, 3, 4, 5];
let b = a;
console.log(b);

function outer(){
    console.log("i am outer");

    return function inner(){
        console.log("inner");
    }
}

let v = outer();
v();