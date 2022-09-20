GCC := g++ --std=c++17 -Werror -Wall

main: main.o thing.o
	@echo "-- main"
	$(GCC) -o main main.o thing.o

main.o: main.cpp
	@echo "-- main.o"
	$(GCC) -c main.cpp

thing.o: thing.cpp thing.h
	@echo "-- thing.o"
	$(GCC) -c thing.cpp

.PHONY: clean
clean:
	@echo "-- clean"
	rm -f main main.o thing.o

.PHONY: run
run: main
	@echo "-- run"
	./main

