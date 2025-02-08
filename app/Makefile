# Makefile to build app.cpp and place the output in bin

CXX := g++
SRC := src/app.cpp
BIN_DIR := bin
INCLUDE_DIR := ./res
LIB_DIR := ./res

TARGET := $(BIN_DIR)/app
CXXFLAGS := -Wall -Wextra -std=c++17 -I$(INCLUDE_DIR) -L$(INCLUDE_DIR) -lfib

all: $(TARGET)

# Build the target
$(TARGET): $(SRC)
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

clean:
	rm -rf $(BIN_DIR)

# Clean the build
.PHONY: clean all