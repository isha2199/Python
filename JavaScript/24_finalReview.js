for (let i = 0; i < 3; i++) {
    setTimeout(() => 
        console.log(i), 0
    );
}

const obj = {
  name: 'Isha',
  greet: function() {
    return () => console.log(this.name);
  }
};
const fn = obj.greet();
fn();

console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');

const arr = [1, 2, 3, 4, 5];
const result = arr.filter(n => n % 2 === 0).map(n => n * 10);
console.log(result);
