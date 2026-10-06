CC ?= cc
CFLAGS ?= -std=gnu17 -O3 -ffast-math -fno-math-errno -march=native
WARN = -Wno-multichar -Wno-parentheses -Wno-pointer-sign -Wno-return-type -Wno-misleading-indentation -Wno-unknown-pragmas
LDLIBS = -lm

all: echo

# Keep the upstream inference engine unchanged. Build first with the same empty
# system prompt form used by the official IOCCC entry; TCGE policy is supplied
# as runtime input by the integration layer rather than fragile compiler quoting.
echo: prog.c
	$(CC) $(CFLAGS) $(WARN) prog.c -DM=\"model\" -DS='""' -o $@ $(LDLIBS)

echo_openmp: prog.c
	$(CC) $(CFLAGS) $(WARN) -fopenmp prog.c -DM=\"model\" -DS='""' -o $@ $(LDLIBS)

clean:
	rm -f echo echo_openmp
