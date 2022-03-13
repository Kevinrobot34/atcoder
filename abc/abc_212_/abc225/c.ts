import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [n, m] = input[0].split(" ").map(Number);
const b: number[][] = input.slice(1).map(si => si.split(" ").map(Number));

let oi: number = Math.floor(b[0][0] / 7);
let oj: number = b[0][0] % 7;
if (oj == 0) {
    oj = 7;
    oi--;
}

let ans: string;
if (oj + m - 1 <= 7) {
    ans = "Yes"
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if ((i + oi) * 7 + (j + oj) != b[i][j]) {
                ans = "No"
            }
        }
    }
} else {
    ans = "No"
}
console.log(ans);