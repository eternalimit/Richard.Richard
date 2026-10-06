CC ?= cc
CFLAGS ?= -std=gnu17 -O3 -ffast-math -fno-math-errno -march=native
WARN = -Wno-multichar -Wno-parentheses -Wno-pointer-sign -Wno-return-type -Wno-misleading-indentation -Wno-unknown-pragmas
LDLIBS = -lm
TCGE_PROMPT = You are an independent TCGE Echo validator. Separate evidence from inference. Return PASS only when the supplied evidence independently supports the candidate; otherwise return HOLD and state missing evidence.

all: echo

echo: prog.c
	$(CC) $(CFLAGS) $(WARN) prog.c -DM=\"model\" -DS='\"$(TCGE_PROMPT)\"' -o $@ $(LDLIBS)

echo_openmp: prog.c
	$(CC) $(CFLAGS) $(WARN) -fopenmp prog.c -DM=\"model\" -DS='\"$(TCGE_PROMPT)\"' -o $@ $(LDLIBS)

clean:
	rm -f echo echo_openmp
