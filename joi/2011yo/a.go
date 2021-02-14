package main

import "fmt"

func main() {
	var a, b, c, d int
	fmt.Scan(&a, &b, &c, &d)
	ans := a + b + c + d
	fmt.Println(ans / 60)
	fmt.Println(ans % 60)
}
