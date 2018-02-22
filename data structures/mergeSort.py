def mergeSort(array, low, high):
	mid = (low + high)//2
	if(low<high):
		mergeSort(array, low, mid)
		mergeSort(array, mid+1, high)
		merge(array,low, mid, high)	

def merge(array, low, mid, high):
	size1 = mid - low + 1
	size2 = high - mid
	arr1 =[None]*size1
	arr2 =[None]*size2

	for i in range(0, size1, 1):
		arr1[i] = array[low + i]
	for i in range(0, size2, 1):
		arr2[i] = array[mid + i +1]
	
	i = j = k = 0

	while (i < size1 and j< size2):		
		if(arr1[i] < arr2[j]):
			array[k+low] = arr1[i]
			k += 1
			i += 1
		elif(arr1[i] > arr2[j]):
			array[k+low] = arr2[j]
			k += 1
			j += 1	
		elif(arr1[i] == arr2[j]):
			array[k+low] = arr1[i]
			k += 1
			array[k+low] = arr2[j]
			i += 1
			k += 1
			j += 1
	while i < size1:
		array[k+low] = arr1[i]
		k += 1
		i += 1
	while j < size2:
		array[k+low] = arr2[j]
		k += 1
		j += 1

array = [3, 25, 12, 22, 11, 2, 1, 33 ,1]
print(array)
mergeSort(array, 0, (len(array)-1))
print(array)				
				