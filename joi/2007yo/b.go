package main

import "fmt"

const n = 30

func main() {
	l := make([]int, n-2)
	for i := 0; i < n-2; i++ {
		fmt.Scan(&l[i])
	}
	for i := 1; i <= n; i++ {
		is_lacked := true
		for _, lj := range l {
			if i == lj {
				is_lacked = false
				break
			}
		}
		if is_lacked {
			fmt.Println(i)
		}
	}
}
