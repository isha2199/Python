function memoise(fn){
    const cache = {};
    return function(...args){
        const key = JSON.stringify(args);
        if(key in cache){
            return cache[key];
        }

        const result = fn.apply(this,args);
        cache[key]= result;

        return result;
    }
}

function sqaure(n){
    console.log("calculating... ");
    return n*n;
}

const memoSq = memoise(sqaure);
console.log(memoSq(5));
console.log(memoSq(5));
console.log(memoSq(10));
