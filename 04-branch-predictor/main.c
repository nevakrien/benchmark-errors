#include <stdio.h>
#include <stdint.h>
#include <time.h>

volatile uint64_t x = 0;

void run_branch_test(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) return;

    uint8_t byte;
    while (fread(&byte, 1, 1, f) == 1) {
        if (byte)
            x++;
        else
            x += 2;
    }

    fclose(f);
}

int main(int argc, char **argv) {
    if (argc != 2) return 1;

    clock_t start = clock();

    run_branch_test(argv[1]);

    clock_t end = clock();

    printf("result: %ld\n",x);
    printf("%.8f\n", (double)(end - start) / CLOCKS_PER_SEC);
    return 0;
}
