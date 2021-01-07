# https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html

import random, time

def bubbleSort(arr): # compares adjacent elements
    for i in reversed(range(0, len(arr))):
        for j in range(1,i+1):
            if arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
    print("Bubble Sort:    ", arr)

def selectionSort(arr): # moves the minimum value to the start
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    print("Selection Sort: ", arr)

def insertionSort(arr): # inserts element in right place compared to previous elements
    for i in range(1,len(arr)):
        index = arr[i]
        j = i
        while j > 0 and arr[j-1] > index:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = index
    print("Insertion Sort: ", arr)

def merge(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSort(a):
    n = len(a)
    step = 1
    while (step < n): # merge two adjacent groups of size 2, then of size 4, then 8, ...
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge(a, start1, start2, end)
        step *= 2

def createArr(length):
    return random.sample(range(1,100), length)

def testSortingAlgorithms():
    newArr = createArr(6) # assume none are the same
    print("Shuffled:\t\t", newArr, "\n")
    
    # Bubble Sort - 0(n^2)
    arr = newArr
    time0 = time.time()
    bubbleSort(arr)
    time1 = time.time()
    print((time1-time0)/1000, " s")
    
    # Selection Sort - 0(n^2)
    arr = newArr
    time0 = time.time()
    selectionSort(arr)
    time1 = time.time()
    print((time1-time0)/1000, " s")
    
    # Insertion Sort - 0(n^2)
    arr = newArr
    time0 = time.time()
    insertionSort(arr)
    time1 = time.time()
    print((time1-time0)/1000, " s")   
    
    # Merge Sort - 0(n ln x)
    arr = newArr
    time0 = time.time()
    mergeSort(arr)
    time1 = time.time()
    print((time1-time0)/1000, " s")   
    
testSortingAlgorithms()