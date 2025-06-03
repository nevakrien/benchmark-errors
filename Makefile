# Top-level Makefile -------------------------------------------------

# Pick up any dir like “01-something/”, “02-something/”, …
SUBDIRS := $(patsubst %/,%,$(dir $(wildcard [0-9][0-9]-*/Makefile)))

all:
	@echo "Building: $(SUBDIRS)"
	@for d in $(SUBDIRS); do \
		$(MAKE) -C $$d; \
	done

bench:
	@echo "Benchmarking: $(SUBDIRS)"
	@for d in $(SUBDIRS); do \
		$(MAKE) -C $$d bench; \
	done

clean:
	@echo "Cleaning: $(SUBDIRS)"
	@for d in $(SUBDIRS); do \
		$(MAKE) -C $$d clean; \
	done
