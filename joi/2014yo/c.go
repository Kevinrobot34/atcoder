package main

import "fmt"

func abs(x int) int {
	if x < 0 {
		x *= -1
	}
	return x
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func dist(x1, y1, x2, y2 int) int {
	if x2 >= x1 && y2 >= y1 {
		x := x2 - x1
		y := y2 - y1
		return min(x, y) + abs(x-y)
	} else if x2 <= x1 && y2 <= y1 {
		x := x1 - x2
		y := y1 - y2
		return min(x, y) + abs(x-y)
	} else {
		return abs(x1-x2) + abs(y1-y2)
	}
}

func main() {
	var w, h, n int
	fmt.Scan(&w, &h, &n)
	var xPrev, yPrev, xCurr, yCurr int
	fmt.Scan(&xPrev, &yPrev)
	ans := 0
	for i := 1; i < n; i++ {
		fmt.Scan(&xCurr, &yCurr)
		ans += dist(xPrev, yPrev, xCurr, yCurr)
		xPrev, yPrev = xCurr, yCurr
	}
	fmt.Println(ans)
}
