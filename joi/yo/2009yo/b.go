package main

import (
	"fmt"
	"sort"
)

const n = 10

func solve() int {
	score := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&score[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(score)))
	ans := score[0] + score[1] + score[2]
	return ans
}

func main() {
	scoreW := solve()
	scoreK := solve()
	fmt.Println(scoreW, scoreK)
}
