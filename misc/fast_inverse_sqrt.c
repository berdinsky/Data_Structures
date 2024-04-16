/* source -  the internet */
#include <stdint.h>
#include <stdio.h>

float FastInvSqrt(float number) {
    int32_t i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y  = number;
    i  = *(int32_t *) &y;                       // evil floating point bit level hacking
    i  = 0x5f3759df - (i >> 1);                 // what the heck?
    y  = *(float *) &i;
    y  = y * (threehalfs - (x2 * y * y));       // 1st iteration of Newton-Raphson method

    return y;
}

int main() {
   float x = 1000.123456F;
   float inv_sqrtx;

   inv_sqrtx = FastInvSqrt(x);
   printf("The inverse square root of %.6f is %.6f.",x,inv_sqrtx);
   printf("\n");

   return 0;
}
