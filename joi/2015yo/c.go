package main

import "fmt"

func main() {
	var h, w int
	fmt.Scan(&h, &w)
	for i := 0; i < h; i++ {
		var cloudi string
		fmt.Scan(&cloudi)

		cnt := -1
		for j, cloudij := range cloudi {
			if cloudij == 'c' {
				cnt = 0
			}
			fmt.Print(cnt)
			if j == w-1 {
				fmt.Print("\n")
			} else {
				fmt.Print(" ")
			}
			if cnt != -1 {
				cnt++
			}
		}
	}
}
