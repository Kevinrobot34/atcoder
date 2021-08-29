package main

import "fmt"

func main() {
	var a, b, c, ans int

	fmt.Scan(&a, &b, &c)
	ans = 21 - a - b - c
	fmt.Println(ans)
}
