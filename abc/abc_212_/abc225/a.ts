import * as fs from 'fs';

const s: string = fs.readFileSync("/dev/stdin", "utf8").trim();

let ans: number;
if (s[0] === s[1] && s[1] === s[2]) {
    ans = 1
} else if (s[0] !== s[1] && s[1] !== s[2] && s[2] !== s[0]) {
    ans = 6
} else {
    ans = 3
}

console.log(ans);