package main

import "fmt"

const unit = 60

func timeToSec(h, m, s int) int {
	return h*unit*unit + m*unit + s
}

func calc(h1, m1, s1, h2, m2, s2 int) (int, int, int) {
	diff := timeToSec(h2, m2, s2) - timeToSec(h1, m1, s1)
	return diff / (unit * unit), (diff % (unit * unit) / unit), diff % unit
}

func main() {
	for i := 0; i < 3; i++ {
		var h1, m1, s1, h2, m2, s2 int
		fmt.Scan(&h1, &m1, &s1, &h2, &m2, &s2)
		h, m, s := calc(h1, m1, s1, h2, m2, s2)
		fmt.Println(h, m, s)
	}
}
