package main

import "fmt"

const MAX = 101

func main() {
	var n, m int
	cntA := make([]int, MAX)
	cntB := make([]int, MAX)
	fmt.Scan(&n, &m)
	for i := 0; i < n; i++ {
		var ai int
		fmt.Scan(&ai)
		cntA[ai] += 1
	}
	for i := 0; i < m; i++ {
		var bi int
		fmt.Scan(&bi)
		cntB[bi] += 1
	}
	for i := 0; i < MAX; i++ {
		if cntA[i] > 0 && cntB[i] > 0 {
			fmt.Println(i)
		}
	}
}
