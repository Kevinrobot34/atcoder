import * as fs from 'fs';

const input: string = fs.readFileSync("/dev/stdin", "utf8").trim();
const n: bigint = BigInt(input);

let k: number = 0;
let power2: bigint = 1n;

while (power2 * 2n <= n) {
    power2 *= 2n;
    k++;
}

console.log(k);