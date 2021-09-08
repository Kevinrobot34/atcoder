package main

import "fmt"

func main() {
	var n int
	var s, ans string
	fmt.Scan(&n)
	fmt.Scan(&s)
	for i, si := range s {
		if si == '1' {
			if i%2 == 0 {
				ans = "Takahashi"
			} else {
				ans = "Aoki"
			}
			break
		}
	}
	fmt.Println(ans)
}
