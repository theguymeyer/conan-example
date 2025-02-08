#!/bin/bash

conan create . fib/1.1@gmeyer/testing  -s compiler="apple-clang" -s compiler.version="14.0"
