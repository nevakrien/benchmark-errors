CC = gcc
CFLAGS = -O2 -std=c99 -Wall

REPEATS = 32 # MUST be a multiple of 8 for clean ABBABAAB repeats

all: slow fast

slow: slow.c
	$(CC) $(CFLAGS) -o slow slow.c

fast: fast.c
	$(CC) $(CFLAGS) -o fast fast.c

bench: slow fast analyze.py
	rm -f slow.txt fast.txt
	@for i in $(shell seq 0 $$(($(REPEATS) - 1))); do \
		case $$((i % 8)) in \
			0|3|5|6) ./slow >> slow.txt ;; \
			1|2|4|7) ./fast >> fast.txt ;; \
		esac; \
	done
	python3 analyze.py slow.txt fast.txt


clean:
	rm -f slow fast *.txt
