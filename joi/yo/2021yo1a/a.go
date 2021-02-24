package main

import (
	"fmt"
	"sort"
)

func main() {
	abc := make([]int, 3)
	fmt.Scan(&abc[0], &abc[1], &abc[2])
	sort.Ints(abc)
	fmt.Println(abc[1])
}
