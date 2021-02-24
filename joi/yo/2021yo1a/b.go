package main

import (
	"fmt"
	"strings"
)

var (
	n      int
	ans, s string
)

func main() {
	fmt.Scan(&n)
	fmt.Scan(&s)

	cnt := make(map[rune]int)
	for _, si := range s {
		cnt[si] += 1
	}
	for _, ti := range "JOI" {
		ans += strings.Repeat(string(ti), cnt[ti])
	}
	fmt.Println(ans)
}
