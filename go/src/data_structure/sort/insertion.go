package sort

/**
 *	InsertionSort	-	sort array by insertion
 *	@a:	items to be sort
 */
func InsertionSort(a []int) {
	var i, j int

	for i = 1; i < len(a); i++ {
		t := a[i]
		for j = i; j > 0 && a[j-1] > t; j-- {
			a[j] = a[j-1]
		}
		a[j] = t
	}
}
