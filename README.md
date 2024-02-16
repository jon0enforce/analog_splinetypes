# UNDER CONSTRUCTION!!! 
# analog_splinetypes: performance tests...
Why analog? Because we want to classify on elliptic metadata. And define a nested structure(tupel):

first: nested structure for overlap-app(8 classes - word overlap=score-of-fitness)

second: nested structure for synthesis-app -- upper bound - lower bound(steady spline-transition), 6 or 8 attributes(test).
# comments
spline.c +++ calc the spline coefficients a[] b[] c[] d[] +++ templated from snippet: https://gist.github.com/svdamani/1015c5c4b673c3297309 
calc_sequence.c +++ calc the cutpoints 
c2.py +++ ctypes implementation and tests, --such as on performance. 
save_frame.c +++ save the classified spline with their attributes: 
a_frame.c +++ metadata attributes from spline: try with https://github.com/J08nY/ecgen
# little help on theory on metadata:
https://personalpages.manchester.ac.uk/staff/gabor.megyesi/teaching/math32062/j-inv.pdf
https://en.wikipedia.org/wiki/Modular_form
# Synopsis/Command line:
cc -std=c99 -shared calc_sequence.c -o calc.so

cc -std=c99 -shared spline.c -o spline.so

python3 c2.py
