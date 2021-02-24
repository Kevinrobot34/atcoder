package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	var l, a, b, c, d int
	fmt.Scan(&l, &a, &b, &c, &d)
	ans := l - max((a+c-1)/c, (b+d-1)/d)
	fmt.Println(ans)
}
