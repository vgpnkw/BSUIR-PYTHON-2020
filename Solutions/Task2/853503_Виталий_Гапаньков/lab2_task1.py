import sys
import os
import tempfile
import random

class heapnode:
	def __init__(self, item, fileHandler):
		self.item = item
		self.fileHandler = fileHandler


class merge_sort:
	def __init__(self):
		self.sortedTempFileHandlerList = []
		self.getCurrentDir()

	def getCurrentDir(self):
		self.cwd = os.getcwd()

	def heapify(self, arr, i, n):
		left = 2 * i + 1
		right = 2 * i + 2
		if left < n and arr[left].item < arr[i].item:
			smallest = left
		else:
			smallest = i
		if i != smallest:
			(arr[i], arr[smallest]) = (arr[smallest], arr[i])
			self.heapify(arr, smallest, n)

	def constructheap(self, arr):
		l = len(arr) - 1
		mid = l // 2
		while mid >= 0:
			self.heapify(arr, mid, l)
			mid -= 1

	def mergeSort(self, alist):
		if len(alist)>1:
			mid = len(alist)//2
			lefthalf = alist[:mid]
			righthalf = alist[mid:]

			self.mergeSort(lefthalf)
			self.mergeSort(righthalf)

			i=0
			j=0
			k=0
			while i<len(lefthalf) and j<len(righthalf):
				if lefthalf[i]<righthalf[j]:
					alist[k]=lefthalf[i]
					i=i+1
				else:
					alist[k]=righthalf[j]
					j=j+1
				k=k+1

			while i<len(lefthalf):
				alist[k]=lefthalf[i]
				i=i+1
				k=k+1

			while j<len(righthalf):
				alist[k]=righthalf[j]
				j=j+1
				k=k+1

	def mergeSortedtemplefiles(self):
		list1 = []
		sortedoutput = open("numbers.txt",'w')

		for tempFileHandler in self.sortedTempFileHandlerList:
			item = int(tempFileHandler.readline().strip())
			list1.append(heapnode(item, tempFileHandler))

		self.constructheap(list1)
		count = 0


		while True:
			minimum = list1[0]
			if minimum.item == sys.maxsize:
				break
			sortedoutput.write(str(minimum.item) + '\n')
			fileHandler = minimum.fileHandler
			item = fileHandler.readline().strip()
			if not item:
				item = sys.maxsize
			else:
				item = int(item)

			list1[0] = heapnode(item,fileHandler)
			self.heapify(list1,0,len(list1))
		for TempFile in self.sortedTempFileHandlerList:
			TempFile.close()
		sortedoutput.close()

	def	splitFiles(self, largerFileName, smallFileSize):
		largeFileHandler = open("sortfile.txt", 'r')
		tempBuffer = []
		size = 0
		while True:
			number = largeFileHandler.readline()
			if not number:
				break
			tempBuffer.append(number)
			size += 1
			if size % smallFileSize == 0:
				tempBuffer = list(map(int,tempBuffer))
				self.mergeSort(tempBuffer)
				tempBuffer = list(map(str,tempBuffer))
				tempBuffer = "\n".join(tempBuffer)
				temp = tempfile.NamedTemporaryFile(mode='w+t',dir = self.cwd ,delete = True)
				temp.writelines(tempBuffer)
				temp.seek(0)
				self.sortedTempFileHandlerList.append(temp)
				tempBuffer = []


largerFileName = 'sortfile.txt'
with open(largerFileName, 'w') as file:
	file.writelines('{}\n'.format(random.randint(-1000000,1000000)) for _ in range(int(5000000)))
output = 'numbers.txt'
smallFileSize = 500000
obj = merge_sort()
obj.splitFiles(largerFileName,smallFileSize)
obj.mergeSortedtemplefiles()