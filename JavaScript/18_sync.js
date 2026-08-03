function greet(name, callback, calback1){
    let msg = "hello " + name;
    callback(msg);
    calback1(25);
}

function showAge(age){
    console.log(age);
}

function logGreeting(greeting){
    console.log(greeting);
}

greet("Alice",logGreeting,showAge);
