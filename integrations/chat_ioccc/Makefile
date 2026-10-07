CC ?= cc
CFLAGS ?= -std=gnu17 -O3 -ffast-math -fno-math-errno -march=native
WARN = -Wno-multichar -Wno-parentheses -Wno-pointer-sign -Wno-return-type -Wno-misleading-indentation -Wno-unknown-pragmas
LDLIBS = -lm

all: echo

system_prompt.h: SYSTEM_INSTRUCTIONS.txt sync_system_prompt.py
	python3 sync_system_prompt.py

echo: prog.c system_prompt.h
	$(CC) $(CFLAGS) $(WARN) -include system_prompt.h prog.c -DM=\"model\" -o $@ $(LDLIBS)

echo_openmp: prog.c system_prompt.h
	$(CC) $(CFLAGS) $(WARN) -fopenmp -include system_prompt.h prog.c -DM=\"model\" -o $@ $(LDLIBS)

clean:
	rm -f echo echo_openmp
