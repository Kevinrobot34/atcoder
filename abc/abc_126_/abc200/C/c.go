package main

import "fmt"

const c int = 200

func main() {
	var n int

	fmt.Scan(&n)
	cnt := make([]int, c)
	for i := 0; i < n; i++ {
		var ai int
		fmt.Scan(&ai)
		cnt[ai%c]++
	}

	ans := 0
	for _, ci := range cnt {
		ans += ci * (ci - 1) / 2
	}
	fmt.Println(ans)
}
