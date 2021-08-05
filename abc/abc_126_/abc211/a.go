package main

import "fmt"

func main() {
	var a, b int
	var c float64
	fmt.Scanf("%d %d", &a, &b)
	c = float64(a)/3.0 + 2.0*float64(b)/3.0
	fmt.Printf("%f\n", c)
}
