def get_meetings_count(start, end, n):
	sch = []
	for i in range(n):
		sch.append((start[i], end[i]))

	sch.sort(key= lambda x: x[1])
	
	ctr = 1
	prev = sch[0][1]
	for i in range(1, n):
		if sch[i][0] > prev:
			ctr += 1
			prev = sch[i][1]

	return ctr

s = [10, 12, 20]
e = [20, 25, 30]
n = 3
print(get_meetings_count(s, e, n))