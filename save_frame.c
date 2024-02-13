#include <stdio.h>
#include <math.h>
/* calculates the sequence length, to cut off
cc -fPIC -shared -std=c99 calc_sequence.c -o calc_sequence.so
 */
/*save the curves m+m and patterns m*m and returns all m*m patterns */


int save_frame(int count,double *offset1, double *cut1 int *one1, int *two1, int *three1, int four1*, int *five1, int *six1, int *seven1, int *eight1,
double *offset2, double *cut2 int *one2, int *two2, int *three2, int four2*, int *five2, int *six2, int *seven2, int *eight2){


int m=sizeof(&offset);
int k=sizeof(&cut);
if(k!=m){
	return 0; /*error*/
	if (k+sizeof(int)==m){
	    return 1;/*error*/
	}
}	
typedef struct elliptic{
	/*a */
    float a0;
    float b0;
    float c0;
    float d0;
    /*a*x */
    float a1;
    float b1;
    float c1;
    float d1;
    /* cut points */
    double offset;
    double cut;
}
/*+++nested structure+++*/
typedef struct patterns{
     int ifirst;/*tupel */
     int isecond;
     struct elliptic first; /* first of tuple */ 
     struct elliptic second; /* second of tuple */
     float entropy; /*entropy between 0...1 */
     double length; /* = elliptic[isecond].cut - elliptic[ifirst].offset;  characteristic vertical */ 
     int incidence;
}

struct elliptic eclist[m+m];/* max-possible unique */
struct patterns plist[m*m]; /*max-possible combinations*/


for(int i=0; i < m; i++){
    eclist[i].one = one1[i];
    eclist[i].two = two1[i];
    eclist[i].three = three1[i];
    eclist[i].four = four1[i];
    eclist[i].five = five1[i];
    eclist[i].six = six1[i];    
    eclist[i].seven = seven1[i];
    eclist[i].eight = eight1[i];
    eclist[i].offset = offset1[i];
    eclist[i].cut = cut1[i];
}
for(int i=m; i < m+m; i++){
    eclist[i].one = one2[i];
    eclist[i].two = two2[i];
    eclist[i].three = three2[i];f
    eclist[i].four = four2[i];
    eclist[i].five = five2[i];
    eclist[i].six = six2[i];    
    eclist[i].seven = seven2[i];
    eclist[i].eight = eight2[i];
    eclist[i].offset = offset2[i];
    eclist[i].cut = cut2[i];
}
for(int i=0; i < m*m; i++){
    plist[i].ifirst = i;
    plist[i].isecond = m+i;
    plist[i].first = eclist[ifirst];
    plist[i].second = eclist[isecond];
    plist[i].entropy = entropy_function();
    plist[i].length = eclist[isecond].cut - eclist[ifirst].offset;
    plist[i].incidence = count_incidence();
}

doule entropy_function(){
/*nearest neighbor in history/saved, update with mean */
}
double count_incidence(){
/*count how often repear in the history/saved, update with mean */	
}
void clean_mean(){
/* clean the history of entropy and incidence; and start a new classification-record */	
}

FString name = "/home/mem/" + str(m) + ".bin"; /*frame count=stack of structures-count */
malloc sizeof(elliptic)*m)
FILE *file;
file = fopen(name, "wb");
if (file == NULL) return false;
if fwrite(m, sizeof(int), 1, file) != m) return false;
return true;
}
