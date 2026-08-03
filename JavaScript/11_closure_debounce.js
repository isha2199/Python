function debounce(fn, delay){
    let timer;

    return function(...args){
        clearTimeout(timer);

        timer = setTimeout(()=>{
            fn.apply(this, args);
        }, delay);
    }
}
const logDebounce = debounce((val)=>{
    console.log("searchnig = " , val);
}, 500);
logDebounce("H");
logDebounce("He");
logDebounce("Hel");
logDebounce("Hell");
logDebounce("Hello");