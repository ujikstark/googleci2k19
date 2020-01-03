import numpy as np
import matplotlib.pyplot as plt

#Time Bound Computation
#make a data matrix A and B with just python
a = [[12,15],
	 [14,16]]
b = [[18,12],
	 [11,17]]

result = [[0,0],
		  [0,0]]
		  
  
for i in range(len(a)):
	for j in range(len(b[0])):
		for k in range(len(b)):
			result[i][j] += a[i][k] * b[k][j]
		
for x in result:
	x = x

#so i make the result manually to display 
x = [657, 504, 588, 612]

#measure time
data_x = [10,100,1000,10000]

#make a plot
plt.figure(1)
plt.plot(data_x, x, color="red")
plt.title('Time Bound Computation\nJust Python')
plt.xlabel('Times')
plt.ylabel('Input')

#--------------------------------
#multiplication matrix with numpy
c = np.array([(15,25),(27,22)])
d = np.array([(22,28),(26,42)])

e = np.dot(c,d)
f = np.ravel(e)
#make a plot
plt.figure(2)	
plt.plot(data_x, f, color="orange")
plt.title('Time Bound Computation\nWith Numpy')
plt.xlabel('Times')
plt.ylabel('Input')

#display the plot
plt.show()	
