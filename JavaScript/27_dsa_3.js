/**
 * Given a string, find the length of the longest substring without repeating characters.
 * Example: "abcabcbb" → answer: 3 (the substring "abc")
 * Example: "bbbbb" → answer: 1 (the substring "b")
 * Example: "pwwkew" → answer: 3 (the substring "wke")
*/


function longestSubstr(str) {
    let count = 0;
    let left = 0;
    let start = 0;
    const set = new Set();

    for(let right=0 ; right<str.length ; right++){
        while(set.has(str[right])){
            set.delete(str[left]);
            left++;
        }

        set.add(str[right]);
        
        if(right - left + 1 > count){
            count = right-left+1;
            start= left;
        }
    }

    return str.slice(start, start+count);
}

console.log(longestSubstr('abcabcbb'));
console.log(longestSubstr('bbbbb'));
console.log(longestSubstr('pwwkew'));
