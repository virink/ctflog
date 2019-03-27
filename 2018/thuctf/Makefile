
default:object
	@rm m >/dev/null 2>&1 || true
	gcc -Wl,-stack_size,1000000 -framework Tcl -framework Tk -framework SystemConfiguration -framework CoreFoundation -o m m.o

object:
	@rm m.o >/dev/null 2>&1 || true
	gcc -DNDEBUG -DMACOSX -g -fwrapv -O3 -Wall -std=c99 -Wextra -arch x86_64 -DUNIVERSAL=1 \
		-Wsign-compare -Wunreachable-code -Wstrict-prototypes \
		-Wno-unused-result -Wno-unused-parameter -Wno-missing-field-initializers \
		-Wimplicit-function-declaration \
		-I/usr/local/include/python3.6m \
		-I/Users/virink/SourceCodes/python/Python-3.6.6 \
		-I/Users/virink/SourceCodes/python/Python-3.6.6/Objects \
		-I/Users/virink/SourceCodes/python/Python-3.6.6/Include \
		-I/Users/virink/SourceCodes/python/Python-3.6.6/Python \
		-L/usr/local/lib/python3.6/config-3.6m-darwin \
		-c m.c -o m.o
