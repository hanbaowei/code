package container

import (
	"data_structure/utils"
)

type Container interface {
	Empty() bool
	Size() int
	Clear()
	Values() []interface{}
}

func GetSortedValues(c Container, comp utils.Comparator) []interface{} {
	v := c.Values()
	if len(v) < 2 {
		return v
	}
	utils.Sort(v, comp)
	return v
}
