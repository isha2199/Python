var varName = 10;
function b(){
    console.log(varName);
}
function fn() {
    var varName;
    console.log(varName);
    b();
}
fn();


let fruits = "apple";
console.log(fruits);
{
    console.log(fruits); // Temporal Dead zone
    let fruits;
    console.log(fruits);
    fruits = "banana";
    console.log(fruits);
}
console.log(fruits);