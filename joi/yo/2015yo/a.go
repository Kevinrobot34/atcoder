package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	var a, b, c, d, p int
	fmt.Scan(&a, &b, &c, &d, &p)
	ans := min(a*p, b+d*max(0, p-c))
	fmt.Println(ans)
}
