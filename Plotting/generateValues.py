import sys
import random

x = 500
y = 250
delta = 10
delta3 = 100
accuracy1 = 50
accuracy2 = 10
accuracy3 = 800

if __name__ == '__main__':
    if len(sys.argv) == 4:
        try:
            len1 = int(sys.argv[1])
            len2 = int(sys.argv[2])
            mode = int(sys.argv[3])
            if mode == 1:
                file = open('data1.txt','w')
                str = "{},{}\n".format(x,y)
                file.write(str)
                for i in range(len1):
                    x += delta
                    str = "{},{}\n".format(x + random.randint(-accuracy1,accuracy1),y + random.randint(-accuracy1,accuracy1))
                    file.write(str)
                for i in range(len2):
                    y += delta
                    str = "{},{}\n".format(x + random.randint(-accuracy1,accuracy1),y + random.randint(-accuracy1,accuracy1))
                    file.write(str)
            if mode == 2:
                file = open('data2.txt','w')
                str = "{},{}\n".format(x,y)
                file.write(str)
                for i in range(len1):
                    x += delta
                    str = "{},{}\n".format(x + random.randint(-accuracy2,accuracy2),y + random.randint(-accuracy2,accuracy2))
                    file.write(str)
                for i in range(len2):
                    y += delta
                    str = "{},{}\n".format(x + random.randint(-accuracy2,accuracy2),y + random.randint(-accuracy2,accuracy2))
                    file.write(str)
            if mode == 3:
                file = open('data3.txt','w')
                str = "{},{}\n".format(x,y)
                file.write(str)
                for i in range(len1):
                    x += delta3
                    str = "{},{}\n".format(x + random.randint(-accuracy3,accuracy3),y + random.randint(-accuracy3,accuracy3))
                    file.write(str)
                for i in range(len2):
                    y += delta3
                    str = "{},{}\n".format(x + random.randint(-accuracy3,accuracy3),y + random.randint(-accuracy3,accuracy3))
                    file.write(str)
        except:
            print("Error")
    else:
        print("More arguments")
