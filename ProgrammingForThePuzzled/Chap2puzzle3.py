def bestTime(schedule):
	times = []
	for t in schedule:
		times.append((t[0],t[2],'start'))
		times.append((t[1],t[2],'end'))
	qsort(times, 0, len(times)-1)
	maxWeight, time = chooseTime(times)
	print("Best time to attend party is at",time,"& the weight is",maxWeight)

def qpartition(array,l, h):
	pivot = array[h][0]
	i = l-1
	j = l
	while j <h:
		if array[j][0] <= pivot:
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

def chooseTime(times):
	currentWeight = time = maxWeight = 0
	for t in times:
		if t[2] == 'start':
			currentWeight += t[1]
		else:
			currentWeight -= t[1]	
		if currentWeight > maxWeight:
			maxWeight = currentWeight
			time = t[0]
	return maxWeight, time

sched3	=	[(6.0,	8.0,	2),	(6.5,	12.0,	1),	(6.5,	7.0,	2),
(7.0,	8.0,	2),	(7.5,	10.0,	3),	(8.0,	9.0,	2),
(8.0,	10.0,	1),	(9.0,	12.0,	2),
(9.5,	10.0,	4),	(10.0,	11.0,	2),
(10.0,	12.0,	3),	(11.0,	12.0,	7)]	
bestTime(sched3)			
