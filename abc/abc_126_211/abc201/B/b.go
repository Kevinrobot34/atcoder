package main

import (
	"fmt"
	"sort"
)

type Mountain struct {
	name   string
	height int
}

func main() {
	var n int

	fmt.Scan(&n)

	mountains := make([]Mountain, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&mountains[i].name, &mountains[i].height)
	}
	sort.Slice(mountains, func(i, j int) bool {
		return mountains[i].height > mountains[j].height
	})

	fmt.Println(mountains[1].name)
}
