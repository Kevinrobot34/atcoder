package main

import (
	"fmt"
	"sort"
)

func main() {
	var a, b, c, n int
	fmt.Scan(&n, &a, &b, &c)
	d := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&d[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(d)))

	calorie := make([]int, n+1)
	cost := make([]int, n+1)
	calorie[0] = c
	cost[0] = a
	ans := 0
	for i, di := range d {
		calorie[i+1] = calorie[i] + di
		cost[i+1] = cost[i] + b
		if calorie[ans]*cost[i+1] < calorie[i+1]*cost[ans] {
			ans = i + 1
		}
	}
	fmt.Println(calorie[ans] / cost[ans])
}
