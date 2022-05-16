import * as fs from 'fs';

const inputs: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const array = new Set(inputs.slice(1))
console.log(array.size);