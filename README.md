# UNDER CONSTRUCTION!!! Next update 28.2. on save_frame.c (datatype)
synthesis: lagrange on 16 coefficients with pattern-overlapp(free scalable, also for quantum-modulation)


AI-digital approach: 3 FEATURES: (x1), (x2), (x3):::

(x1)^3   =  c*(x1)^2

(x2)^3   =  b*(x2)

c*(x3)^2 = b*(x3)

note: try random forest with 3 features (independent variables)

AI-analog approach: Energy fluctutations sum up...(nano/pico-volts<=>32bit/64-bit-AD): A stack of these with same input-line(~zero capacity/nanowire?) for quantum computers?

# analog_splinetypes: performance tests...
Why analog? Because we want to classify on elliptic metadata, and the piece-wise-polynoms(splines) are free scalable. 
# comments
spline.c +++ calc the spline coefficients a[] b[] c[] d[] +++ templated from snippet: https://gist.github.com/svdamani/1015c5c4b673c3297309 
calc_sequence.c +++ calc the cutpoints 
c2.py +++ ctypes implementation and tests, --such as on performance. 
save_frame.c +++ save the classified spline with their attributes: 
a_frame.c +++ metadata attributes from spline: try with https://github.com/J08nY/ecgen
# little help on theory on metadata:
https://personalpages.manchester.ac.uk/staff/gabor.megyesi/teaching/math32062/j-inv.pdf

...and groebner basis:

http://www.math.uni-rostock.de/~nesselmann/KommAlgebra/GroebnerBasen.pdf

and what's this?...

https://inria.hal.science/hal-00819337/document

https://opus4.kobv.de/opus4-zib/frontdoor/index/index/year/1996/docId/247
# Synopsis/Command line:
cc -std=c99 -shared calc_sequence.c -o calc.so

cc -std=c99 -shared spline.c -o spline.so

python3 c2.py
