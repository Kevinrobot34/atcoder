package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	score := make([]int, n)
	for i := 0; i < n*(n-1)/2; i++ {
		var ai, bi, ci, di int
		fmt.Scan(&ai, &bi, &ci, &di)
		ai--
		bi--
		if ci > di {
			score[ai] += 3
		} else if ci == di {
			score[ai]++
			score[bi]++
		} else {
			score[bi] += 3
		}
	}
	for i := 0; i < n; i++ {
		rank := 1
		for j := 0; j < n; j++ {
			if score[j] > score[i] {
				rank++
			}
		}
		fmt.Println(rank)
	}
}
