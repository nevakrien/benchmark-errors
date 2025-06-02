CC = gcc
CFLAGS = -O2 -g -std=c99 -Wall

REPEATS = 128  # MUST be a multiple of 8 for clean ABBABAAB repeats
ANALYZER = ../analyze.py

all: main slow

main: main.c
	$(CC) $(CFLAGS) -o main main.c

slow: slow.c
	$(CC) $(CFLAGS) -o slow slow.c

bench-main: main $(ANALYZER) predictable.bin random.bin
	@echo "\033[1;36m==> Running benchmark with ABBABAAB pattern ($(REPEATS) trials)\033[0m"
	rm -f slow.txt fast.txt
	@for i in $(shell seq 0 $$(($(REPEATS) - 1))); do \
		case $$((i % 8)) in \
			0|3|5|6) ./main random.bin >> slow.txt ;; \
			1|2|4|7) ./main predictable.bin >> fast.txt ;; \
		esac; \
	done
	@echo "\033[1;36m==> Analyzing results...\033[0m"
	python3 $(ANALYZER) slow.txt fast.txt

bench-fair: main slow $(ANALYZER) predictable.bin random.bin
	@echo "\033[1;36m==> Running benchmark with ABBABAAB pattern ($(REPEATS) trials)\033[0m"
	rm -f slow.txt fast.txt
	@for i in $(shell seq 0 $$(($(REPEATS) - 1))); do \
		case $$((i % 8)) in \
			0|3|5|6) ./slow random.bin >> slow.txt ;; \
			1|2|4|7) ./main random.bin >> fast.txt ;; \
		esac; \
	done
	@echo "\033[1;36m==> Analyzing results...\033[0m"
	python3 $(ANALYZER) slow.txt fast.txt

bench: main slow $(ANALYZER) predictable.bin random.bin
	@echo "\033[1;36m==> Running benchmark with ABBABAAB pattern ($(REPEATS) trials)\033[0m"
	rm -f slow.txt fast.txt
	@for i in $(shell seq 0 $$(($(REPEATS) - 1))); do \
		case $$((i % 8)) in \
			0|3|5|6) ./slow predictable.bin >> slow.txt ;; \
			1|2|4|7) ./main random.bin >> fast.txt ;; \
		esac; \
	done
	@echo "\033[1;36m==> Analyzing results...\033[0m"
	python3 $(ANALYZER) slow.txt fast.txt

clean:
	rm -f main slow *.txt
