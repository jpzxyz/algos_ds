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

### The Size of the Problem

f(n) = 2 + 2(n) 

n in this equation represents the size of the problem.
In mathematical notation this is shown as

T(n) = 2 + 2(n)

__nested1.py__

This algorithm features two loops. 
The first loop is flat, but the second contains a loop, nested within a loop, nested within a loop. 

The size of this problem is

T(n) = n + n^3

Clearly, the complexity in the second loop dominates the first.
So much so, that counting the steps in the first loop is trivial.
We will honor counting steps for the foundation it provides, but abandon it for the more relevant measurement of the size of the problem: The order of magnitude.
We'll measure order of magnitude using Big O notation, which is a way to express an algorithm's efficency.
