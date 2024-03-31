import concurrent.futures
import time
import multiprocessing
from multiprocessing import Pool


def factorize(*number):
    list=[]
    for item in number:
        list.append(item)
    for item in list:
        result=[]
        for i in range(1,item+1):
            if item%i==0:
                result.append(i)
        print(result)



if __name__ == '__main__':
    cpu_cores=multiprocessing.cpu_count()
    print(f"CPU cores: {cpu_cores}")
    timer=time
    time_start=timer.time()
    factorize(128, 255, 99999, 10651060)
    print(f"Without multiprocessing: {timer.time()-time_start}")
    time_start1=timer.time()
    with concurrent.futures.ProcessPoolExecutor(2) as executor:
        executor.map(factorize(128, 255, 99999, 10651060))
    print(f"With multiprocessing: {timer.time()-time_start1}")
    time_start2=timer.time()
    with Pool(processes=2) as pool:
        pool.map(factorize,(128,255,99999,10651060))
    print(f"With pool: {timer.time()-time_start2}")
    