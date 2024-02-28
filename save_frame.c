#include <stdio.h>
#include <math.h>
/* calculates the sequence length, to cut off
cc -fPIC -shared -std=c99 calc_sequence.c -o calc_sequence.so
 */
/*save the curves m+m and patterns m*m and returns all m*m patterns */


int save_frame(int count, float *offset1, float *b1, float *c1, float *offset2, float *b2, float *c2, float *offset3){


int m=count;

	
typedef struct elliptic{
	/*fluctuation estimator(dynamic standard deviation estimator) */
    float b;
    float c;
    /*fluctuation bound(dynamic bound on special overlapping-distributions) */
    float bbound;
    float cbound;
    /* offstets */
    float offset;
    float cut;
};
/*+++nested structure+++*/
typedef struct patterns{
     int ifirst;/*tupel */
     int isecond;
     struct elliptic first; /* first of tuple */ 
     struct elliptic second; /* second of tuple */
     float entropy; /*entropy if -999 = spaceholder/not capable */
     float length; /* = elliptic[isecond].cut - elliptic[ifirst].offset;  characteristic vertical */ 
     int incidence;
};

struct elliptic eclist[m+m];/* max-possible unique */
struct patterns plist[m*m]; /*max-possible combinations*/


/* first(tupel) */
for(int i=0; i < m; i++){
    eclist[i].b = b1[i];
    eclist[i].c = c1[i];
    eclist[i].offset = offset1[i];
    eclist[i].cut = offset2[i];
}
/*second(tupel) */
for(int i=m; i < m+m; i++){
    eclist[i].b = b2[i];
    eclist[i].c = c2[i];
    eclist[i].offset = offset2[i];
    eclist[i].cut = offset3[i];
}
for(int i=0; i < m*m; i++){
    plist[i].ifirst = i;
    plist[i].isecond = m+i;
    plist[i].first = eclist[i];
    plist[i].second = eclist[m+i];
    plist[i].length = eclist[m+i].cut - eclist[i].offset;
    plist[i].incidence += 1; 
}

char name[] = "";
sprintf(name,"/home/mem/%d.bin",m); /*frame count=stack of structures-count */
FILE *file;
file = fopen(name, "wb");
/* ... */

return 1;
}
