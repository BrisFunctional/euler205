/*

Calculate frequency distribution, then sum combined frequency.

$ gcc -std=c99 frequency-205.c -O3

*/

#include <stdio.h>
#include <math.h>

#define MAX (6 * 6 + 1)

int lookupPeter[MAX];
int lookupColin[MAX];

int main()
{
    for (int i0 = 1; i0 <= 4; i0++)
    for (int i1 = 1; i1 <= 4; i1++)
    for (int i2 = 1; i2 <= 4; i2++)
    for (int i3 = 1; i3 <= 4; i3++)
    for (int i4 = 1; i4 <= 4; i4++)
    for (int i5 = 1; i5 <= 4; i5++)
    for (int i6 = 1; i6 <= 4; i6++)
    for (int i7 = 1; i7 <= 4; i7++)
    for (int i8 = 1; i8 <= 4; i8++)
        lookupPeter[i0 + i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8]++;

    for (int i0 = 1; i0 <= 6; i0++)
    for (int i1 = 1; i1 <= 6; i1++)
    for (int i2 = 1; i2 <= 6; i2++)
    for (int i3 = 1; i3 <= 6; i3++)
    for (int i4 = 1; i4 <= 6; i4++)
    for (int i5 = 1; i5 <= 6; i5++)
        lookupColin[i0 + i1 + i2 + i3 + i4 + i5]++;

    double cumulativeColin = 0;
    double probabilityPeter = 0;

    double totalPeter = pow(4, 9);
    double totalColin = pow(6, 6);

    for (int i = 0; i < MAX; i++)
    {
        probabilityPeter += lookupPeter[i] / totalPeter * cumulativeColin;
        cumulativeColin  += lookupColin[i] / totalColin;
    }

    printf("%.7f\n", probabilityPeter);

    return 0;
}
