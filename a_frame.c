#include <stdio.h>
#include <math.h>
/* calculates the sequence length, to cut off
cc -fPIC -shared -std=c99 calc_sequence.c -o calc_sequence.so
 */

/* returns n+n (elliptic)spline ranges of coef. The attribute calculation: */ 

double* a_frame(int m, float* one1, float* two1, float* three1, float* four1, float* five1, float* six1, float* seven1, float* eight1,  ){
    float* d;
	for(int i=0; i < m; i++){ /* set calculate the step-sizes - increased/decreased gradient  */		
			d1[i] = five1[i] - one1[i];
			d2[i] = six1[i] - two1[i];
			d3[i] = seven1[i] - three1[i];
			d4[i] = eight1[i] - four1[i];
    }			
	for(int i=m; i < m+m; i++){ /* set calculate the step-sizes - increased/decreased gradient  */
			d1[i] = five2[i] - one2[i];
			d2[i] = six2[i] - two2[i];
			d3[i] = sevent2[i] - three2[i];
			d4[i] = eight2[i] - four2[i];
	}
return d;
}
