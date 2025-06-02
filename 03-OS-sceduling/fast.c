#include <stdio.h>
#include <time.h>

void dumb_read(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) return;

    char buf[4096];
    while (fread(buf, 1, sizeof(buf), f) > 0) {
        // do nothing
    }

    fclose(f);
}


int main() {
    volatile int x = 0;

    //make the OS prefer this
    // for(volatile int i=0;i<=5000000;i++);

    //even IO is making it worse
    for (int i = 0; i < 1000; i++){
        dumb_read("junk.txt");
    }

    clock_t start = clock();
    for (int i = 0; i < 5000; i++) {
        x += 1;
    }
    clock_t end = clock();
    printf("result: %d\n",x);
    printf("%.8f\n", (double)(end - start) / CLOCKS_PER_SEC);
    return 0;
}
