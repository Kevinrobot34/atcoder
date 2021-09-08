package main

import "fmt"

func main() {
	var a, b, c int
	var ans string

	fmt.Scan(&a, &b, &c)
	if a*a+b*b < c*c {
		ans = "Yes"
	} else {
		ans = "No"
	}
	fmt.Println(ans)
}
