import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const x: number = Number(input[0]);

let ans: string;
if (x < 40) {
    ans = `${40 - x}`;
} else if (x < 70) {
    ans = `${70 - x}`;
} else if (x < 90) {
    ans = `${90 - x}`;
} else {
    ans = "expert";
}

console.log(ans);
