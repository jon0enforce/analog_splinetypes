from ctypes import CDLL, POINTER
from ctypes import c_size_t, c_float, c_double, c_int, c_bool
import numpy as np
import sympy as sp
from sympy.abc import x,y
from sympy import Poly
from sympy.polys.polyclasses import DMP
from sympy.polys.domains import RR
#from scipy.interpolate import lagrange
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
px = [1,2,3,4,5,6,7,8]

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
    f1 = [float(list4[0])*x**3 + float(list3[0])*x**2 + float(list2[0])*x**1]
    f2 = [float(list4[1])*x**3 + float(list3[1])*x**2 + float(list2[1])*x**1]
    f3 = [float(list4[2])*x**3 + float(list3[2])*x**2 + float(list2[2])*x**1]
    f4 = [float(list4[3])*x**3 + float(list3[3])*x**2 + float(list2[3])*x**1]
    f5 = [float(list4[4])*x**3 + float(list3[4])*x**2 + float(list2[4])*x**1]
    f6 = [float(list4[5])*x**3 + float(list3[5])*x**2 + float(list2[5])*x**1]
    f7 = [float(list4[6])*x**3 + float(list3[6])*x**2 + float(list2[6])*x**1]
    f8 = [float(list4[7])*x**3 + float(list3[7])*x**2 + float(list2[7])*x**1]
    #reduce to constant basis x^3

    g1 = sp.polys.polytools.groebner(f1,x,order='lex',method='buchberger')#order='lex',order='grlex', order='grevlex',
    g2 = sp.polys.polytools.groebner(f2,x,order='lex',method='buchberger')#method='f5b', method='buchberger'
    g3 = sp.polys.polytools.groebner(f3,x,order='lex',method='buchberger')
    g4 = sp.polys.polytools.groebner(f4,x,order='lex',method='buchberger')
    g5 = sp.polys.polytools.groebner(f5,x,order='lex',method='buchberger')
    g6 = sp.polys.polytools.groebner(f6,x,order='lex',method='buchberger')
    g7 = sp.polys.polytools.groebner(f7,x,order='lex',method='buchberger')
    g8 = sp.polys.polytools.groebner(f8,x,order='lex',method='buchberger') 
    #2 variable coefficients left in each g_i ..
    #little test..
    #c1 = np.polyfit(px,list1,3,rcond=None,full=False,w=None,cov=False) # offset
    solution1 = np.array(str(list(g1)).replace("*x", "").replace("1.0**3","").replace("]","").replace("[","").replace("+","").replace("- ","-").split("**2"))
    solution2 = np.array(str(list(g2)).replace("*x", "").replace("1.0**3","").replace("]","").replace("[","").replace("+","").replace("- ","-").split("**2"))
    solution3 = np.array(str(list(g3)).replace("*x", "").replace("1.0**3","").replace("]","").replace("[","").replace("+","").replace("- ","-").split("**2"))
    solution4 = np.array(str(list(g4)).replace("*x", "").replace("1.0**3","").replace("]","").replace("[","").replace("+","").replace("- ","-").split("**2"))
    solution5 = np.array(str(list(g5)).replace("*x", "").replace("1.0**3","").replace("]","").replace("[","").replace("+","").replace("- ","-").split("**2"))
    solution6 = np.array(str(list(g6)).replace("*x", "").replace("1.0**3","").replace("]","").replace("[","").replace("+","").replace("- ","-").split("**2"))
    solution7 = np.array(str(list(g7)).replace("*x", "").replace("1.0**3","").replace("]","").replace("[","").replace("+","").replace("- ","-").split("**2"))
    solution8 = np.array(str(list(g8)).replace("*x", "").replace("1.0**3","").replace("]","").replace("[","").replace("+","").replace("- ","-").split("**2"))
    
    solutionB = np.zeros(8)
    solutionC = np.zeros(8)
    
    solutionB[0] = solution1[0]
    solutionB[1] = solution2[0]
    solutionB[2] = solution3[0]
    solutionB[3] = solution4[0]
    solutionB[4] = solution5[0]
    solutionB[5] = solution6[0]
    solutionB[6] = solution7[0]
    solutionB[7] = solution8[0]
    if len(solution1) > 1:
        solutionC[0] = solution1[1]
    else:
        solutionC[0] = 0.001
    solutionC[1] = solution2[1]
    solutionC[2] = solution3[1]
    solutionC[3] = solution4[1]
    solutionC[4] = solution5[1]
    solutionC[5] = solution6[1]
    solutionC[6] = solution7[1]
    solutionC[7] = solution8[1]


    polyB = np.polyfit(px, solutionB,3,rcond=None,full=False,w=None,cov=False)
    polyC = np.polyfit(px, solutionC,3,rcond=None,full=False,w=None,cov=False)
    
    #redB = sp.polys.polytools.groebner(polyB,x,order='lex',method='buchberger') 
    #redC = sp.polys.polytools.groebner(polyC,x,order='lex',method='buchberger') 
    print(polyB)#this give the capability to free scale the splines, but the default is 8
    print(polyC)#but for the digital AI interface, we take another approach: Three features.
    #And for quantum artificial intelligence (if such exist), we define an alternative.
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    # lagrange for suitable quantum approach / analog modulation 
    
    k = k+1
    #+++elliptic normalization and points:c*y^2=d*x^3+b*x+a c[]*normal[]=[-1,-2,-3,-4,-5,-6,-7,-8]+++
    
file1.close()
file2.close()
file3.close()
file4.close()    
point1 = time.time_ns()
print((point1-point0)/1000000000)
#done on 3GHz intel CPU...
#~10 seconds for 50.000 samples, and polyfit with degree three takes 0.1 seconds at 3GHz. It is as fast as ctypes.
# 1000.000 SPS := 200 seconds for one second samples..(simple sound wave)
#...
# Multiprosessing is not an accurate solution, like AMD-threadripper.
# GOAL: antifuse FPGA samples on kickstarter... with 200x speedup for this spline computation, for one dimensional analog Data computation.
# +++:deviation(calc)+spline+buchberger+elliptic must put into FPGA

print("one")

#result = save_frame.save_frame(X.ctypes.data_as(POINTER(c_double)), X.size)
#if result == True:
#    print("success!")
#else{
#    print("write/read ERROR")}

