def qpartition(array,l, h):
	pivot = array[h]
	i = l-1
	j = l
	while j <h:
		if array[j] <= pivot:
			temp = array[j]
			i += 1
			array[j] = array[i]
			array[i] = temp
		j += 1
	i += 1	
	temp = array[i]
	array[i] = array[h]
	array[h] = temp
	return i

def qsort(array, l, h):
	if l < h:
		pi =  qpartition(array, l, h)
		qsort(array, l, pi-1)
		qsort(array, pi+1, h)

arr=[64, 25, 12, 22, 11]
qsort(arr, 0, len(arr)-1)
print(arr)	
