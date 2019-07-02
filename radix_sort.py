import numpy as np
import time

# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def counting_sort(array, exp1): 
	n = len(array)  
	output = [0] * (n) # The output array elements that will have sorted array 
 
	count = [0] * (10) # initialize count array as 0 

	# Store count of occurrences in count[] 
	for i in range(0, n): 
		index = int((array[i]/exp1)) 
		count[(index)%10] += 1

	# Change count[i] so that count[i] now contains actual 
	# position of this digit in output array 
	for i in range(1,10): 
		count[i] += count[i-1] 

	# Build the output array 
	i = n-1
	while i>=0: 
		index = (array[i]/exp1) 
		output[count[int((index)%10)] - 1] = array[i] 
		count[int((index)%10)] -= 1
		i -= 1

	# Copying the output array to arr[], 
	# so that arr now contains sorted numbers 
	i = 0
	for i in range(0,len(array)): 
		array[i] = output[i] 

 
def radix_sort(array):  
	max1 = max(array) # Find the maximum number to know number of digits

	# Do counting sort for every digit. Note that instead 
	# of passing digit number, exp is passed. exp is 10^i 
	# where i is current digit number 
	exp = 1
	while max1/exp > 0: 
		counting_sort(array,exp) 
		exp *= 10


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
    archive = open("radix_sort" + str(item) + ".txt", 'w')
    crescent, decrescent, aleatory = factory_array(size=item)

############################################################################################################################

    archive.write("10 execuções com array ordenado em ordem crescente: \n")
    print("Array ordenado em ordem crescente")

    for i in range(executions):
        print("Radix sort " + str(i+1) + " de tamanho: " + str(item))

        init_time = time.time()
        radix_sort(array=crescent)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(i+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")

############################################################################################################################

    archive.write("10 execuções com array em ordem decrescente: \n")
    print("Array ordenado em ordem decrescente")

    for j in range(executions):
        print("Radix sort " + str(j+1) + " de tamanho: " + str(item))

        init_time = time.time()
        radix_sort(array=decrescent)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(j+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")

############################################################################################################################

    archive.write("10 execuções com array desordenado: \n")
    print("Array desordenado")
    for k in range(executions):
        print("Radix sort " + str(k+1) + " de tamanho: " + str(item))
        
        init_time = time.time()
        radix_sort(array=aleatory)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(k+1)+"° execução: " + str(total) + "\n")
    
    archive.write("Tamanho do array: " + str(item) + " | Média dos tempos: " + str(all_times / executions) + "\n")
############################################################################################################################
