import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split(" ");
const s: string = input[0];
const t: string = input[1];

const ans: string = (s < t) ? "Yes" : "No";

console.log(ans);