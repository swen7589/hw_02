import csv
import matplotlib.pyplot as plt 

# graph 2 FML

data2File = open ('astros-2.csv')
data2Reader = csv.reader (data2File)
data2Data = list (data2Reader)
data2Data

data3File = open ('astros-3.csv')
data3Reader = csv.reader (data3File)
data3Data = list (data3Reader)
data3Data

x = [2010, 2011, 2012, 2013, 2014, 2015]
y1 = [73+73, 2+2, 0, 1+0, 23+24, 6+6]
y2 = [37+38, 2+1, 0, 0, 16+16, 6+6]
y3 = [13+13, 0, 0, 0, 1+1, 1+1]
y4 = [7+7, 0, 0, 0, 2+2, 0]

plt.plot(x, y1, label = "Apollo Orbit")
plt.plot(x, y2, label = "Amor Orbit")
plt.plot(x, y3, label = "Aten Orbit")
plt.plot(x, y4, label = "Comet Orbit")

plt.title('Asteroids, Meteorites, and Comets and the Years of Discovery')
plt.xlabel('Years of Discovery')
plt.ylabel('Number of Asteroids Discovered')
plt.legend(loc='upper right')
plt.show()

