def addpoly(p1,p2):
	
	l = []
	i = 0
	j= 0

	while i < len(p1) and j < len(p2):
		
		if p1[i][1] == p2[j][1]:
			m = p1[i][0]+p2[j][0] 
			t = (m,p1[i][1])
			if m != 0:
				l.append(t)
			i += 1
			j += 1

		else:
			if p1[i][1] > p2[j][1]:
				l.append((p1[i][0],p1[i][1]))
				i += 1
			
			else:
				l.append((p2[j][0],p2[j][1]))
				j += 1

	while i < len(p1):
		l.append((p1[i][0],p1[i][1]))
		i += 1

	while j < len(p2):
		l.append((p2[j][0],p2[j][1]))
		j += 1
	
	return (l)

def multpoly(p1,p2):
	i = 0
	j = 0
	s = []
	l = []
	w = []
	while i < len(p1):
		while j < len(p2):
			p = p1[i][0]*p2[j][0]
			e = p1[i][1]+p2[j][1]
			j += 1
			l.append((p,e))
		i += 1
		j = 0
	
	for i in range(len(l)):
			m = l[i][1]
			sum = 0
			for j in range(len(l)):
				if l[j][1] == m:
					sum += l[j][0]
			
			w.append((sum,m))
	
	for x in range(len(w)):
		if w[x][0] != 0:
			s.append(w[x])
	
	return(s)