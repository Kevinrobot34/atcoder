import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const s: string[] = input.slice(0, 3);
const t: string = input[3];

const ans: string = t.split("").map(ti => s[Number(ti) - 1]).join("");
console.log(ans);
