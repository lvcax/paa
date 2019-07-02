import numpy as np
import time

# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(array, low, high): 
	i = (low-1)		 # index of smaller element 
	pivot = array[high]	 # pivot 

	for j in range(low, high): 

		# If current element is smaller than or 
		# equal to pivot 
		if (array[j] <= pivot): 
			# increment index of smaller element 
			i = i+1
			array[i], array[j] = array[j], array[i] 

	array[i+1], array[high] = array[high], array[i+1] 
	return i+1 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quick_sort(array, low, high): 
	if (low < high): 
		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(array, low, high) 

		# Separately sort elements before 
		# partition and after partition 
		quick_sort(array, low, pi-1) 
		quick_sort(array, pi+1, high) 

def factory_array(size):
    array = list()
    while len(array) < size:
        array.append(np.random.randint(1, 101))
    return sorted(array), sorted(array, reverse=True), array


# main

sizes = [1000, 10000, 100000, 1000000]
executions = 10
all_times = 0

for item in sizes:
    archive = open("quick_sort" + str(item) + ".txt", 'w')
    crescent, decrescent, aleatory = factory_array(size=item)

############################################################################################################################

    archive.write("10 execuções com array ordenado em ordem crescente: \n")
    print("Array ordenado em ordem crescente")

    for i in range(executions):
        print("Quick sort " + str(i+1) + " de tamanho: " + str(item))

        init_time = time.time()
        quick_sort(array=crescent, low=crescent[0], high=crescent[len(crescent)-1])
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(i+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")

############################################################################################################################

    archive.write("10 execuções com array em ordem decrescente: \n")
    print("Array ordenado em ordem decrescente")

    for j in range(executions):
        print("Quick sort " + str(j+1) + " de tamanho: " + str(item))

        init_time = time.time()
        quick_sort(array=decrescent, low=decrescent[0], high=decrescent[len(decrescent)-1])
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(j+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")

############################################################################################################################

    archive.write("10 execuções com array desordenado: \n")
    print("Array desordenado")
    for k in range(executions):
        print("Quick sort " + str(k+1) + " de tamanho: " + str(item))
        
        init_time = time.time()
        quick_sort(array=aleatory, low=aleatory[0], high=aleatory[len(aleatory)-1])
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(k+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")
############################################################################################################################
