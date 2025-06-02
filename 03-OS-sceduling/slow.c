#include <stdio.h>
#include <time.h>
#include <sched.h>

int main() {
    volatile int x = 0;

    for(int i=0;i<20;i++)
        usleep(7000); 

    clock_t start = clock();
    for (int i = 0; i < 50000; i++) {
        x += 1;
    }
    clock_t end = clock();

    printf("result: %d\n",x);
    printf("%.8f\n", (double)(end - start) / CLOCKS_PER_SEC);
    return 0;
}
