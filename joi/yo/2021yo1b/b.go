package main

import "fmt"

func main() {
	var n int
	var s, ans string
	fmt.Scanf("%d", &n)
	fmt.Scanf("%s", &s)

	if check(n, s) {
		ans = "Yes"
	} else {
		ans = "No"
	}
	fmt.Println(ans)
}

func check(n int, s string) bool {
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				t := fmt.Sprintf("%c%c%c", s[i], s[j], s[k])
				if t == "IOI" {
					return true
				}
			}
		}
	}
	return false
}
