import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const s0: string = input[0];
const s1: string = input[1];
const s2: string = input[2];

let contests = new Set(["ABC", "ARC", "AGC", "AHC"]);

contests.delete(s0);
contests.delete(s1);
contests.delete(s2);

console.log(Array.from(contests.values())[0]);