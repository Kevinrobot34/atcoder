import * as fs from 'fs';

type Name = {
    s: string
    t: string
};

const input: string[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const n: number = Number(input[0]);
let names: Name[] = [];
for (let i: number = 0; i < n; i++) {
    const input_i: string[] = input[i + 1].split(" ");
    const s: string = input_i[0];
    const t: string = input_i[1];
    names.push({ s: s, t: t })
}

let cnt: number = 0;
for (let i: number = 0; i < n; i++) {
    for (let j: number = i + 1; j < n; j++) {
        if (names[i].s === names[j].s && names[i].t === names[j].t) cnt++;
    }
}
const ans: string = (cnt > 0) ? "Yes" : "No";

console.log(ans)