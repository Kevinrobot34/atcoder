package main

import "fmt"

func main() {
	var a, b, c, d, e int
	fmt.Scan(&a, &b, &c, &d, &e)
	ans := 0
	if a < 0 {
		ans += -a * c
		a = 0
	}
	if a == 0 {
		ans += d
	}
	ans += (b - a) * e
	fmt.Println(ans)
}
