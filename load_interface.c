#include <stdio.h>
#include <math.h>
/* calculates the sequence length, to cut off
cc -fPIC -shared -std=c99 calc_sequence.c -o calc_sequence.so
 */

/* load data and ai interface  */
/* 4 dimensional ai-interface: f(x) =a bx + cx^2 + dx^3, a,b,c,d */
/* 4 dimensions as weights? 1,2,4,8? to one dimension.*/
/* two different interfaces */
void interface_frame(double *c){ /* coef.-ranges */
	for(int i=0; i<sizeof(&c)*double){
		+++
	}
	/* (1) interface datatypesspi: */
	/*+++nested structure+++*/
	typedef struct elliptic{
		/*lower bound */
		double one;
		double two;
		double three;
		double four;
		/*upper bound*/
		double five;
		double six;
		double seven;
		double eight;
		/* cut points */
		double offset;
		double cut;
	}
	typedef struct patterns{
		 struct elliptic first; /* first of tuple */ 
		 struct elliptic second; /* second of tuple */
		 float entropy; /*entropy between 0...1 */
		 double length; /* = elliptic[isecond].cut - elliptic[ifirst].offset;  characteristic vertical */ 
		 int incidence;
	}
	int count /* frame counter */
	struct elliptic eclist[m*count];/* max-possible unique from a long term record */
	struct patterns plist[m*m*count]; /*m*m=max-possible combinations from a long term record*/
	/* faster: */
	struct elliptic short_eclist[m] /* max possible in a single frame */
	struct patterns short_plist[(m/2)+1] /* max possible in a single frame */
	
	/* (2) load the patterns */
    /* (3) load the interface TODO: CODE THE INTERFACE WITH IEEE STANDARDS */
}
