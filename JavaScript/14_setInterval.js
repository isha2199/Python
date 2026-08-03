
// setTimerId = setInterval(greet, 2000);

// polyfill of setInterval using setTimeout
function createSetInterval() {
    let intervalId = 0;
    let intervalMap = {};

    function setIntervalPolyfill(callback, delay = 0, ...args){
        var id = intervalId++;

        function repeat(){
            intervalMap[id] = setTimeout(()=>{
                callback(...args);

                if(intervalMap[id]){
                    repeat();
                }
            }, delay);
        }
        repeat();
        return id;
    }

    function clearIntervalPolyfill(intervalId){
        clearTimeout(intervalMap[intervalId]);
        delete intervalMap[intervalId];
    }

    return { setIntervalPolyfill, clearIntervalPolyfill };
}

const { setIntervalPolyfill, clearIntervalPolyfill } = createSetInterval();

let count = 0;
let setTimerId;
function greet() {
    count++;
    console.log("hello");
    if (count >= 3) {
        clearIntervalPolyfill(setTimerId);
    }
}


setTimerId = setIntervalPolyfill(greet, 100);