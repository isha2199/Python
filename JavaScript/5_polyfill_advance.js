// map 
Array.prototype.mapPolyfill = function(callback){
    let newArr = [];

    for(let i=0 ;i<this.length;i++){
        newArr.push(callback(this[i]));
    }
    return newArr;
}

function square(x){
    return x*x;
}

let mapArr = [1,2,3,4,5];
console.log(mapArr.mapPolyfill(square));