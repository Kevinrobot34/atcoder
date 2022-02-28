import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split(" ");
const a: number = Number(input[0]);
const b: number = Number(input[1]);
const c: number = Number(input[2]);

let ans: number = a + (c - a % c) % c;

if (ans > b) {
    ans = -1;
}

console.log(ans);
