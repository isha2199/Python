function once(fn){
    let called = false;
    let result;

    return function(...args){
        if(!called){
            called = true;
            result = fn.apply(this, args);
        }

        return result;
    };
}

const greet = once(function(name){
    console.log("Executing");
    return "Hello " + name;
});

console.log(greet("Isha"));
console.log(greet("Isha"));