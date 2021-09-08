package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)

	ans := a + b + c - min(a, min(b, c))
	fmt.Println(ans)
}
