import numpy as np
import time
 
def heapify(array, n, i): 
	largest = i 
	left = 2 * i + 1	  
	right = 2 * i + 2	  

	if (left < n and array[i] < array[left]): 
		largest = left 

	if (right < n and array[largest] < array[right]): 
		largest = right 

	if (largest != i): 
		array[i], array[largest] = array[largest], array[i]
 
		heapify(array, n, largest) 

def heap_sort(array): 
	n = len(array) 

	for i in range(n, -1, -1): 
		heapify(array, n, i) 

	for i in range(n-1, 0, -1): 
		array[i], array[0] = array[0], array[i]
		heapify(array, i, 0) 

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
    archive = open("heap_sort" + str(item) + ".txt", 'w')
    crescent, decrescent, aleatory = factory_array(size=item)

    archive.write("10 execuções com array ordenado em ordem crescente: \n")
    print("Array ordenado em ordem crescente")

    for i in range(executions):
        print("Heap sort " + str(i+1) + " de tamanho: " + str(item))

        init_time = time.time()
        heap_sort(array=crescent)
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
        heap_sort(array=decrescent)
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
        heap_sort(array=aleatory)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(k+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")
############################################################################################################################
