package main

import "fmt"

func main() {
	var a, b int
	var ans string
	fmt.Scan(&a, &b)
	if a > 0 && b == 0 {
		ans = "Gold"
	} else if a == 0 && b > 0 {
		ans = "Silver"
	} else {
		ans = "Alloy"
	}
	fmt.Println(ans)
}
