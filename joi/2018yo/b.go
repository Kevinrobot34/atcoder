package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	var n, ai int
	fmt.Scan(&n)
	ans := 0
	cnt := 0
	for i := 0; i < n; i++ {
		fmt.Scan(&ai)
		if ai == 1 {
			cnt++
		} else {
			ans = max(ans, cnt)
			cnt = 0
		}
	}
	ans = max(ans, cnt)
	fmt.Println(ans + 1)
}
