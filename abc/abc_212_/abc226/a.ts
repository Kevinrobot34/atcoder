import * as fs from 'fs';

const input: string = fs.readFileSync("/dev/stdin", "utf8").trim();
const x: number = parseFloat(input);

console.log(x.toFixed());