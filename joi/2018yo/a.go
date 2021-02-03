package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	var n, a, b, c, d int
	fmt.Scan(&n, &a, &b, &c, &d)
	ans := min((n+a-1)/a*b, (n+c-1)/c*d)
	fmt.Println(ans)
}
