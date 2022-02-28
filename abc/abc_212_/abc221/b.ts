import * as fs from 'fs';

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const s: string = input[0];
const t: string = input[1];

let cnt: number = 0;
for (let i: number = 0; i < s.length - 1; i++) {
    if (s[i] !== t[i]) {
        if (s[i] === t[i + 1] && s[i + 1] === t[i]) {
            cnt += 1;
            i++;
        } else {
            cnt = -1;
            break;
        }
    }
}
const ans: string = (cnt === 0 || cnt === 1) ? "Yes" : "No";
console.log(ans);