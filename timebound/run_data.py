import csv
import random
import time
import numpy as np

list_number = 0
count_1 = 0
count_2 = 0

#multiply with numpy
a = np.array([(1,4),(3,2)]) #data matrix 1
b = np.array([(3,1),(1,2)]) #data matrix 2

c = np.dot(a,b) # multiply matrix

d = c.reshape(1, -1)[0] #reshape to one row
	
e1 = d[0]-d[1] #result
e2 = d[2]-d[3] #result
	
#-------------------------------------------------

	
#multiply with only python
a = [[3,1], #data matrix 1
	[2,3]]
b = [[1,3], #data matrix 2
	[5,2]]

result = [[0,0], #put the result
		 [0,0]]
		  

#looping multiply matrix
for i in range(len(a)):	
	for j in range(len(b[0])):
		for k in range(len(b)):
			result[i][j] += a[i][k] * b[k][j]
			
row = np.array(result) # make a read as matrix
c = row.reshape(1, -1)[0] #reshape to one row
c1 = c[0]-c[1] # result
c2 = c[2]-c[3] # result
	


result_name = ["list_number", "count_1", "count_2"]

with open('data_computation.csv', 'w') as csv_file: #make a new file
	data_csv = csv.DictWriter(csv_file, fieldnames=result_name)
	data_csv.writeheader()
	
while True:
	
	with open('data_computation.csv', 'a') as csv_file:
		data_csv = csv.DictWriter(csv_file, fieldnames=result_name)
	
		result_value = {
			"list_number": list_number,
			"count_1": count_1,
			"count_2": count_2
		}
	
		data_csv.writerow(result_value)
		print(list_number, count_1, count_2)
		
		
		list_number += 1
		count_1 = count_1 + random.randint(e1,e2)
		count_2 = count_2 + random.randint(c1,c2)
	
	time.sleep(0.1) #speed time
	if list_number == 1000:
		break
