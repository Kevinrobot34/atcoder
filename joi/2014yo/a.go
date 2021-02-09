package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func sum(x []int) int {
	s := 0
	for _, xi := range x {
		s += xi
	}
	return s
}

func main() {
	score := make([]int, 5)
	for i := 0; i < 5; i++ {
		var s int
		fmt.Scan(&s)
		score[i] = max(s, 40)
	}
	ans := sum(score) / 5
	fmt.Println(ans)
}
