package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	var s, ans string
	fmt.Scan(&n)
	fmt.Scan(&s)
	s_splitted := strings.Split(s, "joi")
	ans = strings.Join(s_splitted, "JOI")
	fmt.Println(ans)
}
