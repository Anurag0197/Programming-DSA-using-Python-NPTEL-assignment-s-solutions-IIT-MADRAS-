def orangecap(d):
	
	m = sorted(d.keys())
	z = []
	n=0
	q= []
	o = []

	sum = []

	for x in range(len(m)):
		z.append([])
	
	for i in range(len(m)):
		z[i].append(sorted(d[m[i]].keys()))

	for j in range(len(z)):
		
		h=0
		
		for r in range(len(z[j][0])):
			n=0
			p = z[j][0][h]
	
			if h < len(z[j][0]) - 1:
				h += 1

			for u in range(len(z)):
				if p in z[u][0] and p not in q:
					n += d[m[u]].get(p,0)
			
			q.append(p)
			sum.append(n)

	x = 0
	while x in sum:
		sum.remove(0)

	for i in q:
		if i not in o:
			o.append(i)
		
	s = sum.index(max(sum))
	return (o[s],sum[s])