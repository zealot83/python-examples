#! /usr/bin/python
#import time

myList = [1,6,2,7,3,8,4,5,9,4,1,2,6,9,8,5,6,3,4,5,6,2,1,3,2,5,4,7,6,9]

def displaylines(dislist):
	for starcnt in dislist:
		print("*" * starcnt)

bubbling = True
while (bubbling):
	bubbling = False
	for num in range(1,len(myList)):
		if (myList[num] < myList[num-1]):
			myTemp = myList[num-1]
			myList[num-1] = myList[num]
			myList[num] = myTemp
			bubbling = True
			displaylines(myList)
			#time.sleep(1)
			print