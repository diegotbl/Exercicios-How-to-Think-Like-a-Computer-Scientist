import random
import multiprocessing
import time
import threading


def list_append(count, id, out_list):
    """
    Creates an empty list and then appends a
    random number to the list 'count' number
    of times. A CPU-heavy operation!
    """
    for i in range(count):
        out_list.append(random.random())

def thread():
    size = 10000000 # Number of random numbers to add
    threads = 2 # Number of threads to create
    start = time.time()

	# Create a list of jobs and then iterate through
	# the number of threads appending each thread to
	# the job list
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=list_append(size, i, out_list))
        jobs.append(thread)

    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

    end = time.time()
    print("List processing complete by threads.")
    print("Execution time of thread: {0}".format(end - start))

if __name__ == '__main__':
    size = 10000000   # Number of random numbers to add
    procs = 2   # Number of processes to create
    start = time.time()

    # Create a list of jobs and then iterate through
    # the number of processes appending each process to
    # the job list
    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process(target=list_append,
			                              args=(size, i, out_list))
        jobs.append(process)

    # Start the processes (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the processes have finished
    for j in jobs:
        j.join()

    end = time.time()
    print("List processing complete by multiprocessing.")
    print("Execution time of multiprocess: {0}".format(end - start))

    print()

    thread()
