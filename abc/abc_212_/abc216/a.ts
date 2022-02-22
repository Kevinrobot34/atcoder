import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split(".");
const x: number = Number(input[0]);
const y: number = Number(input[1]);

let ans: string;

if (0 <= y && y <= 2) {
    ans = `${x}-`
} else if (y <= 6) {
    ans = `${x}`
} else {
    ans = `${x}+`
}
console.log(ans)