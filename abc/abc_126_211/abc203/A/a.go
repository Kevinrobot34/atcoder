package main

import "fmt"

func main() {
	var a, b, c, ans int

	fmt.Scan(&a, &b, &c)

	if a == b {
		ans = c
	} else if b == c {
		ans = a
	} else if c == a {
		ans = b
	} else {
		ans = 0
	}
	fmt.Println(ans)
}
