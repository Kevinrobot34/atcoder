import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const k: number = Number(input[0]);
const a: string = input[1].split(" ")[0];
const b: string = input[1].split(" ")[1];

function change_base_to_10(x: string, k: number): number {
    let y: number = 0;
    for (let xi of x) {
        y = y * k + Number(xi);
    }
    return y
}

const ans: number = change_base_to_10(a, k) * change_base_to_10(b, k);
console.log(ans);