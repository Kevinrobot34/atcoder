package main

import (
	"fmt"
)

func main() {
	var a, b int
	var ans string
	fmt.Scan(&a, &b)

	if (a*b)%2 == 0 {
		ans = "Even"
	} else {
		ans = "Odd"
	}
	fmt.Println(ans)
}
