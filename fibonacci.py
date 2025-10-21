#!/usr/bin/env python3

def get_terms():
  
  while True:
    n = input("How many terms of the fibonacci Sequence?")
    if n.isdigit() and int(n) > 0:
      return int(n)
    print("Please enter valid integer.")
  
  else:
    print("Please enter a posisitive integer.")

def fibonacci(n):
  
  a, b = 0,1
  for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
  

def print_fibonacci():
  n = get_terms()
  fibonacci(n)

print_fibonacci()
# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
