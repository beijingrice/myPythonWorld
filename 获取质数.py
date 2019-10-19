import pickle
allNum = []
num = 1
while True:
    try:
        gotIt = 0
        for x in range(num):
            if num % (x + 1) == 0:
                gotIt += 1
        if gotIt == 2:
            allNum.append(num)
            print(num)
        num += 1
    except KeyboardInterrupt:
        writefile = open("质数表.dat","wb+")
        pickle.dump(allNum,writefile)
        writefile.close()