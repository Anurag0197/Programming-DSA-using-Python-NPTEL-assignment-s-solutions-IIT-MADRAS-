def isprime(n):

	count = 1
	for x in range(2,n+1):
		if n%x == 0:
			count += 1

	if count > 2 or n < 2:
		return False

	else:
		return True


def sumprimes(l):

	s = 0
	for x in range(0,len(l)):
		if l[x] > 0:
			m = isprime(l[x])
			if m:
				s += l[x]

	return s

