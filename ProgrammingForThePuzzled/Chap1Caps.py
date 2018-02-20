def pleaseConform(caps):
	start = forward = backward = 0
	intervals = []
	caps = caps + ['END']
	for i in range(1,len(caps),1):
		if caps[start] != caps[i]:
			intervals.append((start, i-1, caps[start]))
			if caps[start] == 'F':
				forward += 1
			if caps[start] == 'B':
				backward += 1
			start = i
#	print(forward)
#	print(backward)
			
	if forward < backward:
		flip = 'F'
	else:
		flip = 'B'
	for t in intervals:
		if t[2] == flip:
			if t[0] == t[1]:
				print('Person at position',t[0],'flip your cap!')
			else:	
				print('People in positions',t[0],'through',t[1],'please flip your caps!')
cap1 = ['F','F','B','H','B','F','B','B','B','F','H','F','F']
pleaseConform(cap1)			 					
				

			
			
