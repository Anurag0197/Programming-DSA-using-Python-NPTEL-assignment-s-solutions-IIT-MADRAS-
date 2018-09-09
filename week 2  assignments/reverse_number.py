def intreverse(n):

	d = len(str(n))

	if d <= 1:
		return n

	else:
		return (intreverse(n%(10**(d-1)))*10 + n//(10**(d-1)))


