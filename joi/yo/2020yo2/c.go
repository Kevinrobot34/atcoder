package main

import "fmt"

func digitSum(x int) int {
	ret := 0
	for x > 0 {
		ret += x % 10
		x = x / 10
	}
	return ret
}

func main() {
	var n int
	fmt.Scan(&n)
	memo := make([]int, n+1)
	for i := 1; i <= n; i++ {
		memo[i]++
		j := i + digitSum(i)
		if j <= n {
			memo[j] += memo[i]
		}
	}
	fmt.Println(memo[n])
}
