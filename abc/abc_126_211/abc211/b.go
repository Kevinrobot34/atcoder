package main

import "fmt"

func main() {
	var s, ans string
	cnt := map[string]int{"H": 0, "2B": 0, "3B": 0, "HR": 0}
	for i := 0; i < 4; i++ {
		fmt.Scan(&s)
		cnt[s]++
	}
	ans = "Yes"
	for _, val := range cnt {
		if val != 1 {
			ans = "No"
			break
		}
	}
	fmt.Println(ans)
}
