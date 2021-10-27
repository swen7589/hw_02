import csv
# graph 1
data1File = open ('astros.csv')
data1Reader = csv.reader (data1File)
data1Data = list (data1Reader)
data1Data

import matplotlib.pyplot as plt 

craft = ['ISS', 'Shenzhou 13']
number = [7, 3]

plt.bar(craft, number)
plt.title('Number of People Currently in Space, Split by Station')
plt.xlabel('Space Station')
plt.ylabel('Numebr of People')
plt.show()
