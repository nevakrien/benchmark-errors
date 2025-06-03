CC = gcc
CFLAGS = -O2 -std=c99 -Wall


SWITCH_SIZE ?= 10000
REPEATS = 256  # MUST be a multiple of 8 for clean ABBABAAB repeats
ANALYZER = ../analyze.py


all: slow fast

code.o: code.c
	$(CC) $(CFLAGS) -c -o code.o code.c


bad-align.c:
	@echo "Generating $@ with $(SWITCH_SIZE) unique case values and payloads..."
	@echo 'int weird_func(int x) {'            > $@
	@echo '  switch(x) {'                      >> $@
	@awk -v n=$(SWITCH_SIZE) 'BEGIN {           \
		srand(42);                              \
		used_case[""] = 1; used_val[""] = 1;    \
		while (count < n) {                     \
			c = int(1e6 + rand() * 9e6);         \
			v = int(1e6 + rand() * 9e6);         \
			if (!(c in used_case) && !(v in used_val)) { \
				printf("    case %d: x += %d; break;\n", c, v); \
				used_case[c]; used_val[v];       \
				count++;                         \
			}                                    \
		}                                        \
	}'                                           >> $@
	@echo '    default: x += 42; break;'         >> $@
	@echo '  } return x; }'                      >> $@

bad-align.o: bad-align.c
	$(CC) -O0 -c -o bad-align.o bad-align.c

good-align.o: good-align.c
	$(CC) $(CFLAGS) -c -o good-align.o good-align.c

slow: main.c bad-align.o code.o
	$(CC) $(CFLAGS) -o slow main.c bad-align.o code.o

fast: main.c good-align.o code.o
	$(CC) $(CFLAGS) -o fast main.c good-align.o code.o

bench: slow fast $(ANALYZER)
	@echo "\033[1;36m==> Running benchmark with ABBABAAB pattern ($(REPEATS) trials)\033[0m"
	rm -f slow.txt fast.txt
	@for i in $(shell seq 0 $$(($(REPEATS) - 1))); do \
		case $$((i % 8)) in \
			0|3|5|6) ./slow >> slow.txt ;; \
			1|2|4|7) ./fast >> fast.txt ;; \
		esac; \
	done
	@echo "\033[1;36m==> Analyzing results...\033[0m"
	python3 $(ANALYZER) slow.txt fast.txt


clean:
	rm -f slow fast *.txt bad-align.c
