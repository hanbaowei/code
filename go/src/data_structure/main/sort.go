package main

import (
	"data_structure/sort"
	"fmt"
)

func main() {
	t := []int{9, 3, 4, 5, 1, 6, 8, 2, 12, 14, 22, 18, 3, 11}
	sort.InsertionSort(t)
	for _, n := range t {
		fmt.Printf("%d ", n)
	}
}
