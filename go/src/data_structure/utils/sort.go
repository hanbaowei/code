package utils

import "sort"

func Sort(v []interface{}, cp Comparator) {
	sort.Sort(sortable{v, cp})
}

type sortable struct {
	v  []interface{}
	cp Comparator
}

func (s sortable) Len() int {
	return len(s.v)
}

func (s sortable) Swap(i, j int) {
	s.v[i], s.v[j] = s.v[j], s.v[i]
}

func (s sortable) Less(i, j int) bool {
	return s.cp(s.v[i], s.v[j]) < 0
}
