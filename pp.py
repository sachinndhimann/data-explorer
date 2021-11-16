import multiprocessing
import timeit
import time
def square(x):
    print("square")
    time.sleep(5)
    return x * x
   
if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=4)
    inputs = [0,1,2,3,4]
    t1=timeit.default_timer()
    outputs = pool.map(square, inputs)
    t2=timeit.default_timer()
    print(t2-t1)
    print("Input: {}".format(inputs))
    print("Output: {}".format(outputs))