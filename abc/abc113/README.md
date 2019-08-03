## ABC113

### C
ソートしたりする．

### D - Number of Amidakuji　(400点)
bitDP
数xが2進数表記で1が隣合うことがあるかどうかは
`x & (x>>1) != 0`
で判定可能
