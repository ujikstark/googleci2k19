import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

#style
plt.style.use('Solarize_Light2')

#make a data
def plotting_time(a):
	plt.cla()
	data_set = pd.read_csv('data_computation.csv')
	x = data_set['list_number']
	y1 = data_set['count_1']
	y2 = data_set['count_2']	
	
	plt.plot(x, y1, label='Python', color='red')
	plt.plot(x, y2, label='Numpy', color='green')
	plt.legend(loc="best")
	plt.title('Time Bound Computation')
	plt.xlabel('Measure Times')
	plt.ylabel('Input Size')
	

#display the plot		
plot_result = FuncAnimation(plt.figure(), plotting_time, interval=200)
plt.show()	
