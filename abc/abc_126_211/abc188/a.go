package main

import (
	"fmt"
)

func abs(x int) int {
	if x >= 0 {
		return x
	}
	return -x
}

func main() {
	var x, y int
	var ans string
	fmt.Scan(&x, &y)

	if abs(x-y) < 3 {
		ans = "Yes"
	} else {
		ans = "No"
	}
	fmt.Println(ans)
}
