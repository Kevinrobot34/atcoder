package main

import "fmt"

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)
	d := a*7 + b
	ans := (c/d)*7 + min((c%d+a-1)/a, 7)
	fmt.Println(ans)
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
