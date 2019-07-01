import numpy as np
import time
from random import shuffle

'''
begin = time.time()
end = time.time()
total = end - begin
'''

def bogo_sort(array):
    while not all(x <= y for x, y in zip(array, array[1:])):
        shuffle(array)
    return array

def factory_array(size):
    array = list()
    while len(array) < size:
        array.append(np.random.randint(1, 101))
    return sorted(array), sorted(array, reverse=True), array

# main

sizes = [1000, 10000, 100000, 1000000]
executions = 10

for item in sizes:
    archive = open("bogo_sort" + item + ".txt", 'w')
    crescent, decrescent, aleatory = factory_array(item)

    archive.write("10 executions with array crescent:")
    for i in range(executions):
        init_time = time.time()
        bogo_sort(crescent)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(i)+"° execution: " + str(total))
    
    archive.write("Array size crescent: " + str(item) + " | Mean of times: " + str(all_times / executions))

    archive.write("10 executions with array decrescent:")
    for i in range(executions):
        init_time = time.time()
        bogo_sort(decrescent)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(i)+"° execution: " + str(total))
    
    archive.write("Array size decrescent: " + str(item) + " | Mean of times: " + str(all_times / executions))

    archive.write("10 executions with array random:")
    for i in range(executions):
        init_time = time.time()
        bogo_sort(aleatory)
        end_time = time.time()
        
        total = end_time - init_time
        all_times += total
        archive.write(str(i)+"° execution: " + str(total))
    
    archive.write("Array size random: " + str(item) + " | Mean of times: " + str(all_times / executions))
