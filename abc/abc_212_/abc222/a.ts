import * as fs from 'fs';

const n: string = fs.readFileSync("/dev/stdin", "utf8").trim();
const ans: string = n.padStart(4, '0')
console.log(ans);