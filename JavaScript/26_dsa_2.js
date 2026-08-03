
function flattenDepth(arr, depth) {
    return arr.reduce((acc, curr) => {
        if (Array.isArray(curr) && depth > 0) {
            acc.push(...flattenDepth(curr, depth-1));
        } else {
            acc.push(curr);
        }

        return acc;
    }, []);
}

const arr = [1, [2, [3, [4, 5]]]];
console.log(flattenDepth(arr, 1)); // [1, 2, [3, [4, 5]]]     -- only 1 level unwrapped
console.log(flattenDepth(arr, 2)); // [1, 2, 3, [4, 5]]        -- 2 levels unwrapped
console.log(flattenDepth(arr, Infinity)); // [1, 2, 3, 4, 5]   -- fully flat