package main

import "fmt"

func main() {
	var a, b, ans int
	fmt.Scan(&a, &b)
	ans = a ^ b
	fmt.Println(ans)
}
