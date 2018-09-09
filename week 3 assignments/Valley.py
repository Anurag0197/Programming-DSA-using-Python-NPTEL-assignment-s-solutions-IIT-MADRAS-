def valley(l):

	if len(l) < 3:								# A list of integers is said to be a valley if it 
		return(False)							# consists of a sequence of strictly decreasing values 																# followed by a sequence of strictly increasing values.				
	
	i = 1										# The decreasing and increasing sequences must be of length at least 2.

	while l[i] < l[i-1]:						# The last value of the decreasing sequence is the first value of the 

		i += 1 									# increasing sequence.				

		if i == len(l):
			return(False)

	else:

		for x in range(i,len(l)):
			if l[x] <= l[x-1]:
				return(False)

		else:
			return(True)

