#ifndef MYLIB_H
#define MYLIB_H

// Function to find the nth Fibonacci number
int fibonacci(int n);

#endif // MYLIB_H

/*
To compile this header file into an archive file, you can use the following commands:

g++ -c mylib.cpp -o mylib.o
ar rcs libmylib.a mylib.o
*/
