package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

func main() {
	var n, aMax, bMin, ans int

	fmt.Scan(&n)
	aMax = 0
	for i := 0; i < n; i++ {
		var ai int
		fmt.Scan(&ai)
		aMax = max(aMax, ai)
	}
	bMin = 1001
	for i := 0; i < n; i++ {
		var bi int
		fmt.Scan(&bi)
		bMin = min(bMin, bi)
	}

	ans = max(0, bMin-aMax+1)
	fmt.Println(ans)
}
