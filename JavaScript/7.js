function outer() {
  let a = 10;
  return function inner() {
    return function innermost() {
      console.log(a);
    }
  }
}

outer()()();