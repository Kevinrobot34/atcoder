package main

import "fmt"

func main() {
	var a, b, c int

	fmt.Scan(&a, &b, &c)

	ans := "No"
	if a-b == b-c {
		ans = "Yes"
	} else if a-c == c-b {
		ans = "Yes"
	} else if b-a == a-c {
		ans = "Yes"
	} else if b-c == c-a {
		ans = "Yes"
	} else if c-a == a-b {
		ans = "Yes"
	} else if c-b == b-a {
		ans = "Yes"
	}
	fmt.Println(ans)
}
