import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split(" ");
const p: number[] = input.map(val => Number(val) - 1);
const alphabet: string = "abcdefghijklmnopqrstuvwxyz";

const ans: string = p.map(pi => alphabet[pi]).join("");
console.log(ans);
