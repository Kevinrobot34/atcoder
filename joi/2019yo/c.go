package main

import "fmt"

func main() {
	var n int
	var s string
	fmt.Scan(&n)
	fmt.Scan(&s)

	i := 0
	ans := 0
	for i < n-1 {

		if s2 := string(s[i : i+2]); s2 == "OX" || s2 == "XO" {
			ans += 1
			i += 2
		} else {
			i += 1
		}
	}
	fmt.Println(ans)
}
