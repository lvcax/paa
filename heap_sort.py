import numpy as np
import time

# Python program for implementation of heap Sort 

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(array, n, i): 
	largest = i # Initialize largest as root 
	l = 2 * i + 1	 # left = 2*i + 1 
	r = 2 * i + 2	 # right = 2*i + 2 

	# See if left child of root exists and is 
	# greater than root 
	if (l < n and array[i] < array[l]): 
		largest = l 

	# See if right child of root exists and is 
	# greater than root 
	if (r < n and array[largest] < array[r]): 
		largest = r 

	# Change root, if needed 
	if (largest != i): 
		array[i], array[largest] = array[largest], array[i] # swap 

		# Heapify the root. 
		heapify(array, n, largest) 

# The main function to sort an array of given size 
def heap_sort(array): 
	n = len(array) 

	# Build a maxheap. 
	for i in range(n, -1, -1): 
		heapify(array, n, i) 

	# One by one extract elements 
	for i in range(n-1, 0, -1): 
		array[i], array[0] = array[0], array[i] # swap 
		heapify(array, i, 0) 

def factory_array(size):
    array = list()
    while len(array) < size:
        array.append(np.random.randint(1, 101))
    return sorted(array), sorted(array, reverse=True), array

'''
# Driver code to test above 
array = [ 12, 11, 13, 5, 6, 7] 
heapSort(array) 
n = len(array) 
print ("Sorted array is") 
for i in range(n): 
	print ("%d" %array[i]), 
# This code is contributed by Mohit Kumra 
'''
# main

sizes = [1000, 10000, 100000, 1000000]
executions = 10
all_times = 0

for item in sizes:
    archive = open("heap_sort" + str(item) + ".txt", 'w')
    crescent, decrescent, aleatory = factory_array(item)

############################################################################################################################

    archive.write("10 execuções com array ordenado em ordem crescente: \n")
    print("Array ordenado em ordem crescente")

    for i in range(executions):
        print("Heap sort " + str(i+1) + " de tamanho: " + str(item))

        init_time = time.time()
        heap_sort(crescent)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(i+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")

############################################################################################################################

    archive.write("10 execuções com array em ordem decrescente: \n")
    print("Array ordenado em ordem decrescente")

    for j in range(executions):
        print("Heap sort " + str(j+1) + " de tamanho: " + str(item))

        init_time = time.time()
        heap_sort(decrescent)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(j+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")

############################################################################################################################

    archive.write("10 execuções com array desordenado: \n")
    print("Array desordenado")
    for k in range(executions):
        print("Heap sort " + str(k+1) + " de tamanho: " + str(item))
        
        init_time = time.time()
        heap_sort(aleatory)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(k+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")
############################################################################################################################
