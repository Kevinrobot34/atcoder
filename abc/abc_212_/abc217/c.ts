import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const n: number = Number(input[0]);
const p: number[] = input[1].split(" ").map(val => Number(val) - 1);
const p_inv: number[] = new Array(n);

p.forEach((v, i) => { p_inv[v] = i; });
const ans: string = p_inv.map(v => v + 1).join(' ');
console.log(ans);
