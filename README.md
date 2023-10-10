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

### Orders of Magnitude

## Constant Time

T(n) = 1

No matter the inputs, there is always one step. 
Constant complexity is O(1).
It's the most efficient an algorithm can hope to be.

## Logarithmic Time

Logarithmic time grows in proporiton to the logarithm of the input size. 
Binary search is logarithmic. 

T(n) = O(log n)

As the data grows, the number of steps required to output the algorithm grows slowly.

## Linear Time

Linear time grows in proportion of a given input. 
An input of 30 will require 30 steps, for example.

The number of steps of a linear time algorithm might look like

f(n) = 1 + 1 + n

In big O notation we ignore the constants and focus on the most dominant complexity in the algorithm.

O(n) = n

## Log-Linear Time

This algorithm grows as a multiplication of logarithmic and linear time complexities. 

O(n) = O(n log n)

Log-linear algorithms will break data sets into smaller parts, then calculate each piece independently.
Merge sort is log-linear.

## Quadratic (Polynomial) Time

In quadratic time the algorithm is directly proportional to the problem's size squared.

O(n) = O(n^2)

```
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    for j in list:
        x = i * j
        print(x)
```

Every number is multiplied by every other number and the result is stored in a variable. 
In this algorithm, n is the size of the list.

f(n) = 1 + n * n * (1 + 1)

In big O notation we only care about the most complex portion of the equation:

O(n) = n^2

## Cubic Time

In big O notation cubic time is represented as

O(n) = O(n^3)

or

O(n) = n^3

Cubic time's performance is directly proportional to the size of the problem, cubed.

