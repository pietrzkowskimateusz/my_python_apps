import sys
import random

x = 300
y = 260
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
                file = open('data21.txt','w')
                str = "{},{}\n".format(x,y)
                file.write(str)
                for i in range(len1):
                    x += delta
                    y += delta/2
                    str = "{},{}\n".format(x + random.randint(-accuracy1,accuracy1),y + random.randint(-accuracy1,accuracy1))
                    file.write(str)
            if mode == 2:
                file = open('data22.txt','w')
                str = "{},{}\n".format(x,y)
                file.write(str)
                for i in range(len1):
                    x += delta
                    y += delta/2
                    str = "{},{}\n".format(x + random.randint(-accuracy2,accuracy2),y + random.randint(-accuracy2,accuracy2))
                    file.write(str)
            if mode == 3:
                file = open('data23.txt','w')
                str = "{},{}\n".format(x,y)
                file.write(str)
                for i in range(len1):
                    x += delta3
                    y += delta3/2
                    str = "{},{}\n".format(x + random.randint(-accuracy3,accuracy3),y + random.randint(-accuracy3,accuracy3))
                    file.write(str)
        except:
            print("Error")
    else:
        print("More arguments")
