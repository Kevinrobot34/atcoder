import * as fs from 'fs';

const input = fs.readFileSync("/dev/stdin", "utf8").trim().split(" ");
const n: number = +input[0];

let ans: number;

if (n <= 125) {
    ans = 4;
} else if (n <= 211) {
    ans = 6;
} else {
    ans = 8;
}

console.log(ans);