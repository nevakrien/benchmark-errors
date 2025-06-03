int weird_func(int a);
int hot_func(int a,int b);

#include <time.h>
#include <stdio.h>

int main() {
	int x = 0;

	clock_t start = clock();
    for (int i = 0; i < 1000; i++) {
        x = hot_func(i,x);
    }
    clock_t end = clock();

    x =weird_func(x);

    printf("result: %d\n",x);
    printf("%.8f\n", (double)(end - start) / CLOCKS_PER_SEC);
    return 0;
}