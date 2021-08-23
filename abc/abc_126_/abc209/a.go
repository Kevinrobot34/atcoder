package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)
	ans := max(b-a+1, 0)
	fmt.Println(ans)
}
