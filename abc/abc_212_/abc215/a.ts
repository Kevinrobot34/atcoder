import * as fs from 'fs';

const s: string = fs.readFileSync("/dev/stdin", "utf8").trim();
const t: string = "Hello,World!";

const ans: string = (s === t) ? "AC" : "WA";

console.log(ans);