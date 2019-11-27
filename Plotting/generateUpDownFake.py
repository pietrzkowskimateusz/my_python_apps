import sys
import random

x = 250
y = 250
x0=x1=x2=x3=x
y0=y1=y2=y3=y
delta = 10
delta3 = 100
accuracy1 = 50
accuracy2 = 10
accuracy3 = 800

randomowa = []

if __name__ == '__main__':
    if len(sys.argv) == 5:
        try:
            len1 = int(sys.argv[1])
            len2 = int(sys.argv[2])
            len3 = int(sys.argv[3])
            len4 = int(sys.argv[4])

            for i in range(2*len1):
                randomowa.append(random.randint(0,accuracy2/5))

            # Ścieżka
            # # if mode == 0:
            #     file = open('UpDown/data0.txt','w')
            #     str = "{},{}\n".format(x,y)
            #     file.write(str)
            #     for j in range(4):
            #         for i in range(len1):
            #             x += delta
            #             str = "{},{}\n".format(x,y)
            #             file.write(str)
            #         for i in range(len2):
            #             y += delta
            #             str = "{},{}\n".format(x,y)
            #             file.write(str)
            #         for i in range(len1):
            #             x -= delta
            #             str = "{},{}\n".format(x,y)
            #             file.write(str)
            #         for i in range(len2):
            #             y += delta
            #             str = "{},{}\n".format(x,y)
            #             file.write(str)
            #     for i in range(len1):
            #         x += delta
            #         str = "{},{}\n".format(x,y)
            #         file.write(str)
            # # RTLS
            # if mode == 1:
            #     file = open('UpDown/data1.txt','w')
            #     str = "{},{}\n".format(x,y)
            #     file.write(str)
            #     for j in range(4):
            #         for i in range(len1):
            #             x += delta
            #             str = "{},{}\n".format(x + random.randint(-accuracy1,accuracy1),y + random.randint(-accuracy1,accuracy1))
            #             file.write(str)
            #         for i in range(len2):
            #             y += delta
            #             str = "{},{}\n".format(x + random.randint(-accuracy1,accuracy1),y + random.randint(-accuracy1,accuracy1))
            #             file.write(str)
            #         for i in range(len1):
            #             x -= delta
            #             str = "{},{}\n".format(x + random.randint(-accuracy1,accuracy1),y + random.randint(-accuracy1,accuracy1))
            #             file.write(str)
            #         for i in range(len2):
            #             y += delta
            #             str = "{},{}\n".format(x + random.randint(-accuracy1,accuracy1),y + random.randint(-accuracy1,accuracy1))
            #             file.write(str)
            #     for i in range(len1):
            #         x += delta
            #         str = "{},{}\n".format(x + random.randint(-accuracy1,accuracy1),y + random.randint(-accuracy1,accuracy1))
            #         file.write(str)
            # # Odometria
            # if mode == 2:
            #     file = open('UpDown/data2.txt','w')
            #     str = "{},{}\n".format(x,y)
            #     file.write(str)
            #     for j in range(4):
            #         for i in range(len1):
            #             x += delta
            #             str = "{},{}\n".format(x + random.randint(-accuracy2,accuracy2),y + random.randint(-accuracy2,accuracy2))
            #             file.write(str)
            #         for i in range(len2):
            #             y += delta
            #             str = "{},{}\n".format(x + random.randint(-accuracy2,accuracy2),y + random.randint(-accuracy2,accuracy2))
            #             file.write(str)
            #         for i in range(len1):
            #             x -= delta
            #             str = "{},{}\n".format(x + random.randint(-accuracy2,accuracy2),y + random.randint(-accuracy2,accuracy2))
            #             file.write(str)
            #         for i in range(len2):
            #             y += delta
            #             str = "{},{}\n".format(x + random.randint(-accuracy2,accuracy2),y + random.randint(-accuracy2,accuracy2))
            #             file.write(str)
            #     for i in range(len1):
            #         x += delta
            #         str = "{},{}\n".format(x + random.randint(-accuracy2,accuracy2),y + random.randint(-accuracy2,accuracy2))
            #         file.write(str)
            # # GPS
            # if mode == 3:
            #     file = open('UpDown/data3.txt','w')
            #     str = "{},{}\n".format(x,y)
            #     file.write(str)
            #     for j in range(4):
            #         for i in range(len1):
            #             x += delta3
            #             str = "{},{}\n".format(x + random.randint(-accuracy3,accuracy3),y + random.randint(-accuracy3,accuracy3))
            #             file.write(str)
            #         for i in range(len2):
            #             y += delta3
            #             str = "{},{}\n".format(x + random.randint(-accuracy3,accuracy3),y + random.randint(-accuracy3,accuracy3))
            #             file.write(str)
            #         for i in range(len1):
            #             x -= delta3
            #             str = "{},{}\n".format(x + random.randint(-accuracy3,accuracy3),y + random.randint(-accuracy3,accuracy3))
            #             file.write(str)
            #         for i in range(len2):
            #             y += delta3
            #             str = "{},{}\n".format(x + random.randint(-accuracy3,accuracy3),y + random.randint(-accuracy3,accuracy3))
            #             file.write(str)
            #     for i in range(len1):
            #         x += delta3
            #         str = "{},{}\n".format(x + random.randint(-accuracy3,accuracy3),y + random.randint(-accuracy3,accuracy3))
            #         file.write(str)
            # Ścieżka
            # if mode == 0:
            file0 = open('UpDown2/data0.txt','w')
            str0 = "{},{}\n".format(x,y)
            file0.write(str0)
            for j in range(4):
                for i in range(len1):
                    x0 += delta
                    str0 = "{},{}\n".format(x0,y0)
                    file0.write(str0)
                for i in range(len2):
                    y0 += delta
                    str0 = "{},{}\n".format(x0,y0)
                    file0.write(str0)
                for i in range(len1):
                    x0 -= delta
                    str0 = "{},{}\n".format(x0,y0)
                    file0.write(str0)
                for i in range(len2):
                    y0 += delta
                    str0 = "{},{}\n".format(x0,y0)
                    file0.write(str0)
            for i in range(len1):
                x0 += delta
                str0 = "{},{}\n".format(x0,y0)
                file0.write(str0)
            # RTLS
            # if mode == 1:
            file1 = open('UpDown2/data1.txt','w')
            str1 = "{},{}\n".format(x1,y1)
            file1.write(str1)
            for j in range(4):
                for i in range(len1):
                    x1 += delta + randomowa[i]
                    y1 += randomowa[i+len1]
                    str1 = "{},{}\n".format(x1 + random.randint(-accuracy1,accuracy1),y1 + random.randint(-accuracy1,accuracy1))
                    file1.write(str1)
                for i in range(len2):
                    x1 += randomowa[i]
                    y1 += delta + randomowa[i+len1]
                    str1 = "{},{}\n".format(x1 + random.randint(-accuracy1,accuracy1),y1 + random.randint(-accuracy1,accuracy1))
                    file1.write(str1)
                for i in range(len1):
                    x1 -= delta + randomowa[i]
                    y1 += randomowa[i+len1]
                    str1 = "{},{}\n".format(x1 + random.randint(-accuracy1,accuracy1),y1 + random.randint(-accuracy1,accuracy1))
                    file1.write(str1)
                for i in range(len2):
                    x1 += randomowa[i]
                    y1 += delta + randomowa[i+len1]
                    str1 = "{},{}\n".format(x1 + random.randint(-accuracy1,accuracy1),y1 + random.randint(-accuracy1,accuracy1))
                    file1.write(str1)
            for i in range(len1):
                x1 += delta + randomowa[i]
                y1 += randomowa[i+len1]
                str1 = "{},{}\n".format(x1 + random.randint(-accuracy1,accuracy1),y1 + random.randint(-accuracy1,accuracy1))
                file1.write(str1)
            # Odometria
            # if mode == 2:
            file2 = open('UpDown2/data2.txt','w')
            str2 = "{},{}\n".format(x2,y2)
            file2.write(str2)
            for j in range(4):
                for i in range(len1):
                    x2 += delta
                    str2 = "{},{}\n".format(x2 + random.randint(-accuracy2,accuracy2),y2 + random.randint(-accuracy2,accuracy2))
                    file2.write(str2)
                for i in range(len2):
                    y2 += delta
                    str2 = "{},{}\n".format(x2 + random.randint(-accuracy2,accuracy2),y2 + random.randint(-accuracy2,accuracy2))
                    file2.write(str2)
                for i in range(len1):
                    x2 -= delta
                    str2 = "{},{}\n".format(x2 + random.randint(-accuracy2,accuracy2),y2 + random.randint(-accuracy2,accuracy2))
                    file2.write(str2)
                for i in range(len2):
                    y2 += delta
                    str2 = "{},{}\n".format(x2 + random.randint(-accuracy2,accuracy2),y2 + random.randint(-accuracy2,accuracy2))
                    file2.write(str2)
            for i in range(len1):
                x2 += delta
                str2 = "{},{}\n".format(x2 + random.randint(-accuracy2,accuracy2),y2 + random.randint(-accuracy2,accuracy2))
                file2.write(str2)
            # GPS
            # if mode == 3:
            file3 = open('UpDown2/data3.txt','w')
            str3 = "{},{}\n".format(x3,y3)
            file3.write(str3)
            for j in range(4):
                for i in range(len3):
                    x3 += delta3 + 10*randomowa[i]
                    y3 += 10*randomowa[i+len1]
                    # str3 = "{},{}\n".format(x3,y3)
                    str3 = "{},{}\n".format(x3 + random.randint(-accuracy3,accuracy3),y3 + random.randint(-accuracy3,accuracy3))
                    file3.write(str3)
                for i in range(len4):
                    x3 += 10*randomowa[i]
                    y3 += delta3 + 10*randomowa[i+len1]
                    # str3 = "{},{}\n".format(x3,y3)
                    str3 = "{},{}\n".format(x3 + random.randint(-accuracy3,accuracy3),y3 + random.randint(-accuracy3,accuracy3))
                    file3.write(str3)
                for i in range(len3):
                    x3 -= delta3 + 10*randomowa[i]
                    y3 += 10*randomowa[i+len1]
                    # str3 = "{},{}\n".format(x3,y3)
                    str3 = "{},{}\n".format(x3 + random.randint(-accuracy3,accuracy3),y3 + random.randint(-accuracy3,accuracy3))
                    file3.write(str3)
                for i in range(len4):
                    x3 += 10*randomowa[i]
                    y3 += delta3 + 10*randomowa[i+len1]
                    # str3 = "{},{}\n".format(x3,y3)
                    str3 = "{},{}\n".format(x3 + random.randint(-accuracy3,accuracy3),y3 + random.randint(-accuracy3,accuracy3))
                    file3.write(str3)
            for i in range(len3):
                x3 += delta3 + 10*randomowa[i]
                y3 += 10*randomowa[i+len1]
                # str3 = "{},{}\n".format(x3,y3)
                str3 = "{},{}\n".format(x3 + random.randint(-accuracy3,accuracy3),y3 + random.randint(-accuracy3,accuracy3))
                file3.write(str3)
        except:
            print("Error")
    else:
        print("More arguments")
