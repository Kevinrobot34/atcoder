package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func main() {
	var n, ans int

	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		var ai int
		fmt.Scan(&ai)
		ans += max(ai-10, 0)
	}
	fmt.Println(ans)
}
