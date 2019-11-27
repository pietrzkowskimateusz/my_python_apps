import matplotlib.pyplot as plt
import sys

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# anchorsX = (0,5000,5000,0)
# anchorsY = (0,0,5000,5000)
anchorsX = (0,5,5,0)
anchorsY = (0,0,5,5)

try:
    folder = str(sys.argv[1])
except:
    print("Błąd wczytywania parametru")

file0 = (folder+'data0.txt')
file1 = (folder+'data1.txt')
file2 = (folder+'data2.txt')
file3 = (folder+'data3.txt')

data0 = open(file0,'r').read()
lines0 = data0.split('\n')
x0 = []
y0 = []
for line0 in lines0:
    if len(line0) > 1:
        x_0, y_0 = line0.split(',')
        x0.append(float(x_0)/1000)
        y0.append(float(y_0)/1000)

data1 = open(file1,'r').read()
lines1 = data1.split('\n')
x1 = []
y1 = []
for line1 in lines1:
    if len(line1) > 1:
        x_1, y_1 = line1.split(',')
        x1.append(float(x_1)/1000)
        y1.append(float(y_1)/1000)


data2 = open(file2,'r').read()
lines2 = data2.split('\n')
x2 = []
y2 = []
for line2 in lines2:
    if len(line2) > 1:
        x_2, y_2 = line2.split(',')
        x2.append(float(x_2)/1000)
        y2.append(float(y_2)/1000)


data3 = open(file3,'r').read()
lines3 = data3.split('\n')
x3 = []
y3 = []
for line3 in lines3:
    if len(line3) > 1:
        x_3, y_3 = line3.split(',')
        x3.append(float(x_3)/1000)
        y3.append(float(y_3)/1000)



ax1.clear()
# plt.xlim(-0.1, 5.1)
# plt.ylim(-0.1,5.1)
plt.xlabel('x [m]')
plt.ylabel('y [m]')

path, = ax1.plot(x0, y0,'y', linewidth=4)
path.set_label('Ścieżka')

odom, = ax1.plot(x2, y2,'r',linewidth=1)
odom.set_label('Odometria')

ax1.scatter(x1, y1,c='blue',s=10, label='RTLS')

ax1.scatter(x3,y3,c='green',s=20, label='GPS')

ax1.scatter(anchorsX, anchorsY,s=50,c='black', label='Anchors')

plt.legend()
ax1.grid()
plt.show()
