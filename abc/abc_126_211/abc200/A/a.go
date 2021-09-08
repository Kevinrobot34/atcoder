package main

import "fmt"

func main() {
	var n int

	fmt.Scan(&n)
	ans := (n + 100 - 1) / 100
	fmt.Println(ans)
}
