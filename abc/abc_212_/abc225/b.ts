import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const n: number = Number(input[0]);
const edge: number[][] = input.slice(1).map(si => si.split(" ").map(Number));

let ans = "No";
for (let v = 1; v <= n; v++) {
    let check: boolean = true;
    for (let i = 0; i < n - 1; i++) {
        if (!edge[i].includes(v)) {
            check = false;
            break;
        }
    }
    if (check) {
        ans = "Yes"
        break;
    }
}
console.log(ans);