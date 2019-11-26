import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

anchorsX = (0,5000,5000,0)
anchorsY = (0,0,5000,5000)

data1 = open('data21.txt','r').read()
lines1 = data1.split('\n')
x1 = []
y1 = []
for line1 in lines1:
    if len(line1) > 1:
        x_1, y_1 = line1.split(',')
        x1.append(float(x_1))
        y1.append(float(y_1))


data2 = open('data22.txt','r').read()
lines2 = data2.split('\n')
x2 = []
y2 = []
for line2 in lines2:
    if len(line2) > 1:
        x_2, y_2 = line2.split(',')
        x2.append(float(x_2))
        y2.append(float(y_2))


data3 = open('data23.txt','r').read()
lines3 = data3.split('\n')
x3 = []
y3 = []
for line3 in lines3:
    if len(line3) > 1:
        x_3, y_3 = line3.split(',')
        x3.append(float(x_3))
        y3.append(float(y_3))



ax1.clear()
plt.xlim(-100, 5100)
plt.ylim(-100,5100)

ax1.scatter(x1, y1,c='blue', label='RTLS')
# rtls.set_label('RTLS')
odom, = ax1.plot(x2, y2, 'r')
odom.set_label('Odometria')
ax1.scatter(x3,y3,c='green', label='GPS')
# gps.set_label('GPS')
ax1.scatter(anchorsX, anchorsY,c='black', label='Anchors')
plt.legend()
ax1.grid()
plt.show()
