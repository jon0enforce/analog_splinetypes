from ctypes import CDLL, POINTER
from ctypes import c_size_t, c_float, c_double, c_int, c_bool
import numpy as np 
from multiprocessing import Process, Pool, Queue
from functools import partial
import time
import struct
#import Multiprocessing #test this interface
#from sklearn.linear_model import RidgeClassifier#test this interface
#from sklearn.neighbors import KNeighborsClassifier, NearestCentroid#test
#own library
calc_seq = np.ctypeslib.load_library('/home/c/calc', '.')
calc_spline = np.ctypeslib.load_library('/home/c/spline', '.')
#save_frame = np.ctypeslib.load_library('/home/c/save', '.')

#TODO:
#load_interface = np.ctypeslib.load_library('/home/c/load', '.')

calc_seq.argtypes = [POINTER(c_double), c_int]
calc_seq.restype = c_int


calc_spline.argtypes = [POINTER(c_double), c_int, c_int]
calc_spline.restype = c_int

#TODO:
#load_interface.argtypes = [POINTER(c_float)]#argument: [splines range-boundaries a[]+b[]+c[]+d[]

#save_frame.argtypes = [POINTER(c_int), POINTER(c_double),POINTER(c_double), POINTER(c_int),POINTER(c_int), 
#POINTER(c_int),POINTER(c_int), POINTER(c_int),POINTER(c_int), POINTER(c_int),
#POINTER(c_int), POINTER(c_double),POINTER(c_double), POINTER(c_int),POINTER(c_int), POINTER(c_int),POINTER(c_int), 
#POINTER(c_int),POINTER(c_int), POINTER(c_int),POINTER(c_int)]
#save_frame.restype = c_bool #true-saved or false-error


#X = record...data...
#test..
mean = 0
std = 1
num_samples = 1000
samples = np.random.normal(mean, std, num_samples)

t0 = np.linspace(0,10, 50000)#maximum 50.000
t1 = np.linspace(0,62, 50000)
t2 = np.linspace(0,43, 50000)
t3 = np.linspace(0,3, 50000)

s0 = np.sin(t0)
s1 = np.sin(t1)
s2 = np.sin(t2)
s3 = np.sin(t3)

c0 = np.cos(t0)
c1 = np.cos(t1)
c2 = np.cos(t2)
c3 = np.cos(t3)

p0 = s0/c0
p1 = s1/c1
p2 = s2/c2
p3 = s3/c3

rng = np.random.default_rng()
X = np.array(p0)
x0 = np.random.normal(0,p0.std(), t0.size) * 0.04
x1 = np.random.normal(0,p1.std(), t1.size) * 0.15
x2 = np.random.normal(0,p2.std(), t2.size) * 0.1
x3 = np.random.normal(0,p3.std(), t3.size) * 0.05
X = p0 + p1 + p2 + p3
point0 = time.time_ns()
k = 0
coef = np.ndarray((X.size,), dtype=np.float32)

px = (1,2,3,4,5,6,7,8)
print(len(px))
#just for first:
while len(X) > 0:
    values = calc_seq.calc_sequence(X.ctypes.data_as(POINTER(c_double)), X.size)
    CUT = X[:values]
    X = X[values:]
    print(len(X))
    n=X.size
    if len(X) == 0:
        break
    result = calc_spline.spline(CUT.ctypes.data_as(POINTER(c_double)), n, k)
    file1 = open(r"/home/mem/" + str(k) + "a.bin", "rb")#test- take lowest as lower bound -- highest -- upper, 8 values..
    list1 = struct.unpack("f"*result, file1.read(4*result))#and print..
    file2 = open(r"/home/mem/" + str(k) + "b.bin", "rb")#test- take lowest as lower bound -- highest -- upper, 8 values..
    list2 = struct.unpack("f"*result, file2.read(4*result))#and print..
    file3 = open(r"/home/mem/" + str(k) + "c.bin", "rb")#test- take lowest as lower bound -- highest -- upper, 8 values..
    list3 = struct.unpack("f"*result, file3.read(4*result))#and print..
    file4 = open(r"/home/mem/" + str(k) + "d.bin", "rb")#test- take lowest as lower bound -- highest -- upper, 8 values..
    list4 = struct.unpack("f"*result, file4.read(4*result))#and print..
    c1 = np.polyfit(px,list1,3,rcond=None,full=False,w=None,cov=False)
    c2 = np.polyfit(px,list2,3,rcond=None,full=False,w=None,cov=False)
    c3 = np.polyfit(px,list3,3,rcond=None,full=False,w=None,cov=False)
    c4 = np.polyfit(px,list4,3,rcond=None,full=False,w=None,cov=False)    
    k = k+1
    print(c1)
    print(c2)  
    print(c3)
    print(c4)
    #+++elliptic normalization and points:c*y^2=d*x^3+b*x+a c[]*normal[]=[-1,-2,-3,-4,-5,-6,-7,-8]+++
    
file1.close()
file2.close()
file3.close()
file4.close()    
point1 = time.time_ns()
print((point1-point0)/1000000000)
#done on 3GHz intel CPU...
#~1.2+0.8=2 seconds for 50.000 samples, and polyfit with degree three takes 0.1 seconds at 3GHz. It is as fast as ctypes.
# 1000.000 SPS := 40 seconds
# 1000.000.0000 SPS := 400 seconds (Analog-Mono)
# just in time computation needs 80-times-speedup for (Analog-)stereo or 400 speedup for gigabit (Analog)video encoding.
# The goal is 50-500 times speedup. With FPGA. 
# Multiprosessing is not an accurate solution, like AMD-threadripper.
# GOAL: antifuse FPGA samples on kickstarter... with 50x speedup for this spline computation, for one dimensional analog Data computation.
# +++:deviation(calc)+spline+elliptic must put into FPGA

print("one")

#result = save_frame.save_frame(X.ctypes.data_as(POINTER(c_double)), X.size)
#if result == True:
#    print("success!")
#else{
#    print("write/read ERROR")}
