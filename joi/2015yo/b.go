package main

import "fmt"

func game(target int, b []int, score []int) {
	x := 0
	for i, bi := range b {
		if bi == target {
			score[i]++
		} else {
			x++
		}
	}
	score[target-1] += x
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	a := make([]int, m)
	for i := 0; i < m; i++ {
		fmt.Scan(&a[i])
	}

	score := make([]int, n)
	for _, ai := range a {
		b := make([]int, n)
		for j := 0; j < n; j++ {
			fmt.Scan(&b[j])
		}
		game(ai, b, score)
	}

	for _, scorei := range score {
		fmt.Println(scorei)
	}
}
