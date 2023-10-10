# Algorithms and Data Structures

## Algorithms

Algorithms are fundamental to computer science. 
Depending on who you ask, an algorithm is composed of three or four properties.

Definiteness: contains clear, concise, and unambiguous steps 
Effectiveness: Ability to perform precise operations to solve a given problem
Finiteness: The algorithm stops after a finite number of steps
Correctness: An algorithm produces the same output for a given input

### Time

__time.py__

Tracks how long the computer takes to print the given range.
Given a range of 1 to 10, this straightforward algorithm requires 10 steps to complete.
f(n) = 10

__time2.py__

This algorithm initates a count variable and increments the count variable after printing 'i'.
Given a range of 1 to 10, this algorithm has 21 steps. 
f(n) = 1 + 10 + 10

__time3.py__

Changing the range from 1 to 10 to 1 to n changes the number of steps to:
f(n) = 1 + 1 + 2(n)

The additional + 1 is for naming the variable n
