import time
import numpy as np

def brownian_motion(x0,dt,n):
    return x0 + np.sum(np.sqrt(dt)*np.random.normal(0.0,1.0,(x0.size,n)),axis=1)

x0 = np.random.uniform(-1.0,1.0,1000)
dt = 0.0001
n = 10000
start_time = time.time()
start_processing_time = time.process_time()
x = brownian_motion(x0,dt,n)
time_length = time.time()-start_time
processing_time_length = time.process_time() - start_processing_time
print("Mean: %6.3f, Standard Dev: %6.3f, time: %6.3e, process time: %6.3e" %(np.mean(x),np.std(x),time_length,processing_time_length))
