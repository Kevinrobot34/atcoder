import * as fs from 'fs';

const input = fs.readFileSync("/dev/stdin", "utf8").trim().split(" ");
const s: number = +input[0];
const t: number = +input[1];


let ans: number = 0;

for (let a: number = 0; a <= s; a++) {
    for (let b: number = 0; a + b <= s; b++) {
        for (let c: number = 0; a + b + c <= s; c++) {
            if (a * b * c <= t) ans++;
        }
    }
}

console.log(ans);