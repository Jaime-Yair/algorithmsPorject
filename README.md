# Omnidroid Cost Calculator


This project implements a memoized dynamic programming algorithm to calculate the total sprocket cost required to construct an omnidroid. The omnidroid is built from a hierarchical structure of parts, each of which may depend on other parts for its construction.

The program reads an input file containing the details of the omnidroid's parts and dependencies, computes the total cost, and outputs the result in a specified format.

## Files in the project

1. `omnidroid.py`:
   - The main Python script that implements the memoized dynamic programming solution.
  
2.Input File(s):
   - Text files containing information about the parts, dependencies, and sprocket costs. Examples include `example-input.txt` and `big-input.txt`.

## How the Code Works

The program:

1. Parses the input file to extract:
   - The number of parts (n) and dependencies (m).
   - The dependencies of each part.
   - The base sprocket cost of each part.
2. Uses dynamic programming with memoization to compute the total sprocket cost:
   - For each part, the algorithm recursively calculates the cost by summing the cost of its dependencies and its base sprocket cost.
   - Computed results are stored in a memoization dictionary to avoid redundant calculations.
3. Outputs the total cost in the format:



