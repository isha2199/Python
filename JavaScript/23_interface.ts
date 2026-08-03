interface User {
    name: String;
    age: Number;
    email: string
}

function printId(id: string | number){
    if(typeof id === 'string'){
        console.log(id.toUpperCase());
    } else{
        console.log(id.toFixed(2));
    }
}
printId('isha');
printId(20.3901982);
printId(10.99999999);
printId(10.88999999);


function greet(name: string | null) {
  console.log(name?.toUpperCase());
}