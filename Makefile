CC = clang++
CFLAGS = -std=c++26
NOWARN = -Wno-unused-value

main:
	$(CC) $(CFLAGS) $(NOWARN) outputs/$(file).cc -o outputs/$(file).out


run: main
	./outputs/$(file).out

clean:
	rm outputs/*.out