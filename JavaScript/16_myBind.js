Function.prototype.myBind = function(obj){
    const originalFn = this;
    return function(...args){
        return originalFn.call(obj, ...args);
    }
}

function greet(greeting){
    console.log(greeting + ' ' + this.name);
}
const user = {name: "Isha"};

const boundGreet = greet.myBind(user);
boundGreet('Hello');
