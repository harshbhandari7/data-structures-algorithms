from queue import PriorityQueue
arr = [900, 1100, 1235]
dep = [1000, 1200, 1240]

# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]

sch = []
pq = PriorityQueue()

for i in range(len(arr)):
	sch.append((arr[i], dep[i]))

sch.sort(key=lambda x: x[0])

pq.put(sch[0][1])
ctr = 1

for i in range(1, len(sch)):
	top = pq.get()
	pq.put(top)
	if sch[i][0] <= top:
		ctr +=1
	else:
		pq.get()
	
	pq.put(sch[i][1])

print(ctr)
