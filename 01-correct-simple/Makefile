CC = gcc
CFLAGS = -O2 -std=c99 -Wall

REPEATS = 30

all: slow fast

slow: slow.c
	$(CC) $(CFLAGS) -o slow slow.c

fast: fast.c
	$(CC) $(CFLAGS) -o fast fast.c

bench: slow fast analyze.py 
	rm -f slow.txt fast.txt
	for i in $(shell seq 1 $(REPEATS)); do ./slow >> slow.txt; done
	for i in $(shell seq 1 $(REPEATS)); do ./fast >> fast.txt; done
	python3 analyze.py slow.txt fast.txt

clean:
	rm -f slow fast *.txt
