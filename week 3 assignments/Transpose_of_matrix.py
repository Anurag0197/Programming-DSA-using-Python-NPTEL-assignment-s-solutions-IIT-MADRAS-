def transpose(m):

	n = []

	for i  in range(len(m[0])):
		n.append([])

	for i in range(len(m)):
		for j in range(len(m[0])):
			n[j].append(m[i][j])

	return(n)
