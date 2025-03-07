CC = clang++
CFLAGS = -std=c++26

main:
	$(CC) $(CFLAGS) outputs/$(file).cc -o outputs/$(file).out || echo "Error: compilation filed!"


run: main
	./outputs/$(file).out

clean:
	rm outputs/*.out