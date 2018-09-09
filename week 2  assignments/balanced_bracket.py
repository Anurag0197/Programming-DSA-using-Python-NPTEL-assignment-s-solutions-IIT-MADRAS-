def matched(s):
	
	l=[]
	j=-1

	if s[0] == ')' or s[len(s)-1] == '(':
		return False

	for i in range(0,len(s)):
		if s[i] == '(':
			l.append(s[i])
			j += 1 

		elif s[i] == ')':
			if j != -1:
				l.remove(l[j])
				j -= 1

			else:
				return False
	
	if(len(l) == 0):
		return True

	else:
		return False
			

