
function counter(initialVal){

    let count = initialVal;



    return {
        increment() {
            return ++count;
        },
        decrement() {
            return --count;
        },
        getValue(){
            return count;
        }
    }
}

const c = counter(0);
console.log(c.count); // undefined due to closure
c.increment();
c.decrement();
console.log(c.getValue());