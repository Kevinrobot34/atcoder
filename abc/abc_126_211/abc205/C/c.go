package main

import (
	"fmt"
)

func comp(a, b int) string {
	if a < b {
		return "<"
	} else if a == b {
		return "="
	} else {
		return ">"
	}
}

func main() {
	var a, b, c int
	var swp bool
	var ans string

	fmt.Scan(&a, &b, &c)
	swp = false
	if a > b {
		b, a = a, b
		swp = true
	}

	if a >= 0 {
		// 0 <= a <= b
		ans = comp(a, b)
	} else if b >= 0 {
		// a < 0 <= b
		if c%2 == 0 {
			ans = comp(-a, b)
		} else {
			ans = "<"
		}
	} else {
		// a <= b < 0
		if c%2 == 0 {
			ans = comp(-a, -b)
		} else {
			ans = comp(-b, -a)
		}
	}
	if swp {
		if ans == "<" {
			ans = ">"
		} else if ans == ">" {
			ans = "<"
		}
	}
	fmt.Println(ans)
}
