import sys
import random

x = 400
y = 200
x0=x1=x2=x3=x
y0=y1=y2=y3=y
delta = 10
delta3 = 100
accuracy1 = 70
accuracy2 = 5
accuracy3 = 800

randomowa = []

if __name__ == '__main__':
    if len(sys.argv) == 3:
        # try:
        len1 = int(sys.argv[1])
        len2 = int(sys.argv[2])

        for i in range(2*len1):
            randomowa.append(random.randint(0,accuracy2/5))
        # Ścieżka
        # if mode == 0:
        file0 = open('Line2/data0.txt','w')
        str0 = "{},{}\n".format(x0,y0)
        file0.write(str0)
        for i in range(len1):
            x0 += delta
            # y0 += delta/2
            str0 = "{},{}\n".format(x0,y0)
            file0.write(str0)
        # RTLS
        # if mode == 1:
        file1 = open('Line2/data1.txt','w')
        str1 = "{},{}\n".format(x1,y1)
        file1.write(str1)
        for i in range(len1):
            x1 += delta + randomowa[i]
            y1 += randomowa[i+len1]
            str1 = "{},{}\n".format(x1,y1 + random.randint(-accuracy1,accuracy1))
            file1.write(str1)
        # Odometria
        # if mode == 2:
        file2 = open('Line2/data2.txt','w')
        str2 = "{},{}\n".format(x2,y2)
        file2.write(str2)
        for i in range(len1):
            x2 += delta
            # y2 += delta/2
            str2 = "{},{}\n".format(x2 + random.randint(-accuracy2,accuracy2),y2 + random.randint(-accuracy2,accuracy2))
            file2.write(str2)
        # GPS
        # if mode == 3:
        file3 = open('Line2/data3.txt','w')
        str3 = "{},{}\n".format(x3,y3)
        file3.write(str3)
        for i in range(len2):
            x3 += delta3 + randomowa[i]
            y3 += randomowa[i+len1]
            str3 = "{},{}\n".format(x3 + random.randint(-accuracy3,accuracy3),y3 + random.randint(-accuracy3,accuracy3))
            file3.write(str3)
        # except:
            # print("Error")
    else:
        print("More arguments")
