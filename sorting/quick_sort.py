
myList = [1 ,6 ,2 ,7 ,3 ,8 ,4 ,5 ,9 ,4 ,1 ,2 ,6 ,9 ,8 ,5 ,6 ,3 ,4 ,5 ,6 ,2 ,1 ,3 ,2 ,5 ,4 ,7 ,6 ,9]


def displaylines(dislist):
    #for starcnt in dislist:
        #print("*" * starcnt)
    print


def partition(qlist, qfirst, qlast):
    # qpivot = qlist[qfirst + (qlast - qfirst) / 2]
    qpivot = qlist[qfirst]
    print("P using first value for pivot: " + str(qpivot))
    i = qfirst +1
    j = qlast
    quickining = True
    while quickining:
        print("P org -- i= " +str(i))
        while ((i <= j) and (qlist[i] <= qpivot)):
            # print("P while qlist[i]: " + str(qlist[i]) + " <= qpivot:" + str(qpivot))
            i += 1
        print("P new -> i= " +str(i))
        # print "P qlist[" + str(i) + "]:" + str(qlist[i]) + " is greater than the pivot:" + str(qpivot)
        # print "P 	OR i="+str(i)+" equals j="+str(j)

        print("P org -- j= " +str(j))
        while (qlist[j] >= qpivot and j >= i):
            # print("P while qlist[j]:" + str(qlist[j]) + " >= qpivot:" + str(qpivot))
            j -= 1
        print("P new <- j= " +str(j))
        # print "P qlist[" + str(j) + "]:" + str(qlist[j]) + " is less than the pivot:" + str(qpivot)
        # print "P 	OR i="+str(i)+" equals j="+str(j)

        print("P new i= " +str(i ) +" <> j= " +str(j))
        if (j < i):
            print("P done partitioning for now")
            quickining = False
        else:
            print("P swapping qlist positions: i= " +str(i ) +" j= " +str(j))
            print("P swapping qlist[i]:" + str(qlist[i]) + " with qlist[j]:" + str(qlist[j]))
            print("P org qlist:" + str(qlist))
            qtmp = qlist[i]
            qlist[i] = qlist[j]
            qlist[j] = qtmp
            print("P new qlist:" + str(qlist))

    qtmp = qlist[j]
    qlist[j] = qpivot
    qlist[qfirst] = qtmp
    print("P final qlist:" + str(qlist))
    print("")
    return j

def quicksort(qlist, qfirst, qlast):
    print("quick processing -> first:" + str(qfirst) + " last:" + str(qlast))
    print(qlist)
    displaylines(qlist)
    if (qfirst < qlast):
        qpivot = partition(qlist, qfirst, qlast)
        print("current pivot point:" + str(qpivot))
        quicksort(qlist, qfirst, qpivot -1)
        print(qlist)
        quicksort(qlist, qpivot +1, qlast)
        print(qlist)
    return myList

newList = quicksort(myList, 0, len(myList) -1)
displaylines(newList)