import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const n: number = Number(input[0]) - 1;
const s: string = input[1];

const ans: string = (s[n] == 'o') ? "Yes" : "No";
console.log(ans);
