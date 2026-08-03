// Given a string, reverse only the vowels
// keeping all other characters in their original positions.
// Example: "hello" → vowels are e, o → reversed → o, e
// result: "holle"


function reverseVowels(str) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
    const chars = str.split("");
    let left = 0;
    let right = chars.length - 1;

    while (left < right) {
        while (left < right && !vowels.has(chars[left])) {
            left++;
        }
        while (left < right && !vowels.has(chars[right])) {
            right--;
        }
        [chars[left], chars[right]] = [chars[right], chars[left]];
        left++;
        right--;
    }

    return chars.join("");
}

console.log(reverseVowels("hello"));
console.log(reverseVowels("hll"));

