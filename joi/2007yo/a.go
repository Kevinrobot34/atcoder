package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	var inf, mat, sci, eng int
	fmt.Scan(&inf, &mat, &sci, &eng)
	a := inf + mat + sci + eng
	fmt.Scan(&inf, &mat, &sci, &eng)
	b := inf + mat + sci + eng
	ans := max(a, b)
	fmt.Println(ans)
}
