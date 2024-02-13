#include <stdio.h>
#include <math.h>
/* calculates the sequence length, to cut off
cc -fPIC -shared -std=c99 calc_sequence.c -o calc_sequence.so
 */

/* gives back offset and cut points: return+returns=cut; offset= sum of previous returns */

int calc_sequence(double *v, int n){
    double v1 = v[0];
    double v2 = v[1];
    double v3 = v[2];
    double d1 = 0;
    double d2 = 0;
    int a = 0;
    int mode = 0;
    int modecheck = 0;
    double square1;
    double square2;
    double root1;
    double root2;

    for (int i = 3; i < n; i++){
        d1 = v1 - v2;
        d2 = v2 - v3;
        square1 = d1*d1;
        square2 = d2*d2;
        root1 = sqrt(square1); 
        root2 = sqrt(square2);
        modecheck = mode;
        if (root1 >= root2){ /* decreased gradient(downwards or upwards) */
            a = a + 1;
            mode = 1;
            /*
            if(v1<v3){ /* increaed-downwards-to-decreased-downwards gradient, but we make it with cubic, up to x^3
				return a+1;
			}
			*/
        }else{ /*increased gradient (downwards or upwards..)*/
            a = a + 1;
            mode = 2;
            /*
            if(v1>v3){ /* increased-upwards-to-decreased-upwards, but we make it with cubic, up to x^3
			    return a+1;
			}
			*/
		}
        if (modecheck != mode && modecheck !=0){return a+1;} /* normal: increase(down.) -- decrease(up.), increase(up.) -- decrease(down.) gradient  */
	/* returns the length of the elliptic-sequence: 6 Cases to break up. Right? */
        v1 = v[i-2];
        v2 = v[i-1];
        v3 = v[i];
    }
return a+3;
}




