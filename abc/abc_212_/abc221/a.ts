import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split(" ");
const a: number = +input[0];
const b: number = +input[1];

const ans: number = Math.pow(32, a - b);
console.log(ans);