console.log("start");
setTimeout(()=>{
    console.log("st1");
},1000);
setTimeout(()=>{
    console.log("st2");
},500);
function sayBye(){
    console.log("bye");
}
sayBye();
console.log("end");

console.log("1");
async function foo(){
    console.log("2");
    await null;
    console.log("3");
}
foo();
console.log("4");

function getData(){
    fetchSomething().then((result) => {
        console.log(result);
    });
}

async function getData(){
    const result = await fetchSomething();
    console.log(result);
}