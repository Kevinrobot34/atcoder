package main

import "fmt"

func main() {
	var s, t string
	var n int
	fmt.Scan(&s)
	fmt.Scan(&n)
	cnt := 0
	for i := 0; i < n; i++ {
		fmt.Scan(&t)
		t = t + t
		for j := 0; j < 10; j++ {
			if s == string(t[j:j+len(s)]) {
				cnt++
				break
			}
		}
	}
	fmt.Println(cnt)
}
