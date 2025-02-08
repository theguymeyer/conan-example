CC = g++
CFLAGS = -Wall -g
TARGET = bin/libfib.a
AR = ar
ARFLAGS = rcs
SRCS = $(wildcard src/*.cpp)
OBJS = $(SRCS:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	@mkdir -p bin
	$(AR) $(ARFLAGS) $@ $^
	rm -f $(OBJS)

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)
	rm -rf bin

.PHONY: all clean