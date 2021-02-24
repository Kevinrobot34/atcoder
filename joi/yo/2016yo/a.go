package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	var a, b, c, d, e, f int
	fmt.Scan(&a, &b, &c, &d, &e, &f)
	ans := a + b + c + d + e + f
	ans -= min(a, min(b, min(c, d)))
	ans -= min(e, f)
	fmt.Println(ans)
}
