Jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
# Jobs = [(1,2,100),(2,1,19),(3,2,27),
#         (4,1,25),(5,1,15)]

Jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = Jobs[0][1]
for i in range(1, len(Jobs)):
	if Jobs[i][1] > max_deadline:
		max_deadline = Jobs[i][1]

slots = [-1] * (max_deadline + 1)

profit = 0
ctr = 0

for i in range(len(Jobs)):
	for j in range(Jobs[i][1], 0, -1):
		if slots[j] == -1:
			slots[j] = Jobs[i][0]
			ctr += 1
			profit += Jobs[i][2]
			break

print(ctr, profit)