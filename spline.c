/** Numerical Analysis 9th ed - Burden, Faires (Ch. 3 Natural Cubic Spline, Pg. 149) */
/** templated from gist.github.com*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
/* cc -std=c99 -shared spline.c -o spline.so */
/* returns all coefficients a[],b[],c[],d[] */
static char* unsigned_to_float_string(uint32_t raw);
int spline(double *a, int n, int count) {
    /** Step 0 */
    int i, j;
    n--;
    float x[n + 1], h[n], A[n], l[n + 1],
        u[n + 1], z[n + 1], c[n + 1], b[n], d[n];
    for (i = 0; i < n + 1; ++i) x[i]=i;
    
    /** Step 1 */
    for (i = 0; i <= n - 1; ++i) h[i] = x[i + 1] - x[i];
    
    /** Step 2 */
    for (i = 1; i <= n - 1; ++i)
        A[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1];
    
    /** Step 3 */
    l[0] = 1;
    u[0] = 0;
    z[0] = 0;
    /** Step 4 */
    for (i = 1; i <= n - 1; ++i) {
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1];
        u[i] = h[i] / l[i];
        z[i] = (A[i] - h[i - 1] * z[i - 1]) / l[i];
    }
    
    /** Step 5 */
    l[n] = 1;
    z[n] = 0;
    c[n] = 0;

    /** Step 6 */
    for (j = n - 1; j >= 0; --j) {
        c[j] = z[j] - u[j] * c[j + 1];
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3;
        d[j] = (c[j + 1] - c[j]) / (3 * h[j]);
    }

    
    char str1[64];
    char str2[64];
    char str3[64];
    char str4[64];
    
    sprintf(str1, "/home/mem/%da.bin", count);
    sprintf(str2, "/home/mem/%db.bin", count);
    sprintf(str3, "/home/mem/%dc.bin", count);
    sprintf(str4, "/home/mem/%dd.bin", count);

    FILE* file1;
    file1 = fopen(str1, "wb");
    if (file1 == NULL) return 0;
    fwrite(&a, sizeof(float), sizeof(a), file1);
    fclose(file1);

    FILE* file2;
    file2 = fopen(str2, "wb");
    if (file2 == NULL) return 0;
    fwrite(&b, sizeof(float), sizeof(b), file2);
    fclose(file2);
    
    FILE* file3;
    file3 = fopen(str3, "wb");
    if (file3 == NULL) return 0;
    fwrite(&c, sizeof(float), sizeof(c), file3);
    fclose(file3);
    
    FILE* file4;
    file4 = fopen(str4, "wb");
    if (file4 == NULL) return 0;
    fwrite(&d, sizeof(float), sizeof(d), file4);           
    fclose(file4);
    
    
    return sizeof(a);
    
}
