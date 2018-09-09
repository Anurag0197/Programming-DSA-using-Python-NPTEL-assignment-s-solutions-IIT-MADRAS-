import sys

i = 0
j = 0
k = 0
a = "0"

courses = []
students = []
grades = []
l = []
score = []
output = []

while True:
	courses.append(sys.stdin.readline())
	a = courses[i]
	i += 1	
	if "Students" in a:
		break

while True:
	students.append(sys.stdin.readline())
	a = students[j]
	j += 1
	if "Grades" in a:
		break

while True:
	grades.append(sys.stdin.readline())
	a = grades[k]
	k += 1
	
	if "EndOfInput" in a:
		break

for i in range(len(students)):
	students[i] = students[i].strip('\n')

for x in range(len(students)-1):
	index = students[x].index("~")

	l.append(students[x][index-7:index])

grades.remove('EndOfInput\n')

for x in range(len(grades)):

	if grades[x][-3] == "~":
		grades[x] = grades[x][-10:len(grades[x])]

	else:
		grades[x] = grades[x][-11:len(grades[x])]
	
students.sort()
grades.sort()
l.sort()


students.remove('Grades')

i = 0
j = 0
sum = 0
k = 0
count = 0

while i < len(l):

	if j < len(grades) and l[i] in grades[j] :
	
		if grades[j][-3] == "~":
				c = grades[j][-2]

		else:
			c = grades[j][-3:-1]

			
		if c == 'A':
			c = 10

		elif c == 'AB':
			c = 9

		elif c == 'B':
			c = 8

		elif c == 'BC':
			c = 7

		elif c == 'C':
			c = 6

		elif c == 'CD':
			c = 5

		else:
			c = 4

		sum += c 	
		count += 1
		j += 1


	else:

		i += 1

		if count != 0:
			avg = sum/count
		else:
			avg = sum

		avg = round(avg,2)
		score.append(str(avg))
		
		sum = 0
		count = 0
	
for i in range(len(students)):
	output.append("~".join([students[i],score[i]]))


for x in range(len(output)):
	sys.stdout.write(output[x])
	sys.stdout.write("\n")