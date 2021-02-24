package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	var a, b, c, d, e int
	fmt.Scan(&a, &b, &c, &d, &e)
	ans := min(a, min(b, c)) + min(d, e) - 50
	fmt.Println(ans)
}
