#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    if length <= 0:
        print( [] )
    elif length == 1:
        print( [0] )
    elif length == 2:
        print( [0,1] )
    else:
        fib = [0,1]
        for num in range( 2, length ):
            fib.append( fib[-2] + fib[-1] )
        print( fib )
