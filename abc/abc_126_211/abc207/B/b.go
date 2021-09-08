package main

import "fmt"

func main() {
	var a, b, c, d int
	fmt.Scan(&a, &b, &c, &d)

	var ans int
	if c*d-b <= 0 {
		ans = -1
	} else {
		ans = (a + (c*d - b) - 1) / (c*d - b)
	}
	fmt.Println(ans)
}
