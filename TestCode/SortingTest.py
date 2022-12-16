
array = [1,2,3,4,5,6,7]
i = 0
j = 5
array

(array[1], array[4]) # (2, 5) ... So... it is making a tuple? Yes... I think. is there a way to test for type / class in python? 
print(type((array[1], array[4]))) # <class 'tuple'> .... so yes a tuple.. once again, things just make sense in python.. wonderful. 

# encountered the below line online... wondering if its valid syntax, and what the heck it actually does. 
(array[i], array[j]) = (array[j], array[i])
array # expecting to see a reordering..? IT WORKS.. now what the heck is up with this syntax? 


# Heap Sort in python

#--------- HEAPSORT -------------------------------------------------------------------------------

def heapify(arr, arrayLength, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < arrayLength and arr[i] < arr[l]:
        largest = l

    if r < arrayLength and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, arrayLength, largest)


def heapSort(arr):
    arrayLength = len(arr)

    # Build max heap
    for i in range(arrayLength//2, -1, -1):
        heapify(arr, arrayLength, i)

    for i in range(arrayLength-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)


arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')

#----------------------------------------------------------------------------------------


for i in range(6//2, -1, -1):
    print(i)

for i in range(6//2, -1):
    print(i)

r = range(3, -1)
for i in r:
    print(i)




