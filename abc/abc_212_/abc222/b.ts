import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const n: number = Number(input[0].split(" ")[0]);
const p: number = Number(input[0].split(" ")[1]);
const a: number[] = input[1].split(" ").map(Number);

const aa: number[] = a.map(ai => (ai < p) ? 1 : 0);
let ans: number = aa.reduce((sum, current) => sum + current, 0);
console.log(ans);