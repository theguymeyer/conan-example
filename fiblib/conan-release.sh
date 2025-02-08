#!/bin/bash
# the reason for the compiler and version hardcoding is because this conan system does not recognize my updated clang version of 15

conan create . fib/1.1@gmeyer/testing  -s compiler="apple-clang" -s compiler.version="14.0"
