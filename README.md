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
   
```An omnidroid with <n> parts and <m> dependencies, takes <X> sprockets to build.```

## Input File Format

The input file should have the following structure:

1. First line: Two integers, n (number of parts) and m (number of dependencies).
2. Next m lines: Pairs of integers, i and j, indicating that part i is used in the construction of part j.
3. Next n lines: Integers indicating the base sprocket cost for each part, in order from part 0 to part n-1.


## How to Compile and Run
1. Prerequisites:
   - Install Python (version 3.6 or higher).
   - Ensure the input file is saved in the same directory as the omnidroid.py script.
2. Running the Script:
   - Open a terminal or command prompt.
   - Navigate to the directory containing omnidroid.py and the input file.
   - Run the script using the command:
      `python omnidroid.py <input_file>`
3. Example Run:
   - For the file example-input.txt:
     `python omnidroid.py example-input.txt`
   - Output
     `An omnidroid with 8 parts and 12 dependencies, takes 100 sprockets to build.`
4. For Other Input Files:
   - Ensure the input file follows the required format.
   - Run the script with the file name as the argument:
      `python omnidroid.py big-input.txt`

## Expected Output
The program prints a message to the console summarizing the number of parts, dependencies, and the total sprocket cost. For example:
`An omnidroid with <n> parts and <m> dependencies, takes <X> sprockets to build.`







