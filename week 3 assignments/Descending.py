def descending(l):
	
	for i in range(1,len(l)):                   # Descending means  each element in input list 
			
		if l[i] > l[i-1]:						# is at most as big as the one before it.
			return(False)

	else:
		return(True)
