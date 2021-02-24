package main

import "fmt"

func main() {
	var a, b, c, ans int
	fmt.Scan(&a, &b, &c)
	cnt := map[int]int{1: 0, 2: 0}
	cnt[a]++
	cnt[b]++
	cnt[c]++
	if cnt[1] > cnt[2] {
		ans = 1
	} else {
		ans = 2
	}
	fmt.Println(ans)
}
