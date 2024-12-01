#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from collections import defaultdict

def read_file(filename):
    
    """
    Parses the input file and returns:
    - n: The number of parts in the assembly
    - m: The number of dependencies
    - dependencies: A dictionary mapping each part to its dependencies
    - sprocket_costs: A list of sprocket costs for each part
    """
    
    # Read the file
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # Read n and m
    n, m = map(int, lines[0].split())
    
    # Read dependencies
    dependencies = defaultdict(list)
    for i in range(1, m + 1):
        part_i, part_j = map(int, lines[i].split())
        dependencies[part_j].append(part_i)
    
    # Read sprocket costs
    #sprocket_costs = list(map(int, lines[m + 1:])) #failed when blank spaces
    
    sprocket_costs = list(map(int, filter(lambda x: x.strip(), lines[m + 1:])))
    
    return n, m, dependencies, sprocket_costs


def calculate_sprockets(part, dependencies, sprocket_costs, memo):
    
    """
    Recursively calculates the total sprocket cost for a given part using memoization.
    - part: The ID of the part to calculate the cost for
    - dependencies: A dictionary of dependencies for all parts
    - sprocket_costs: A list of base sprocket costs
    - memo: A dictionary to store computed costs for memoization
    """
    
    # If result already computed, return it
    if part in memo:
        return memo[part]
    
    # Base case: if no dependencies, cost is directly sprocket_costs[part]
    cost = sprocket_costs[part]
    
    # Add costs of dependencies
    for dependency in dependencies[part]:
        cost += calculate_sprockets(dependency, dependencies, sprocket_costs, memo)
    
    # Memorize and return
    memo[part] = cost
    return cost

def main(filename):
    
    """
    Main function to parse the input file, calculate total sprocket costs,
    and print the required output.
    """
    
    # Parse the input file
    n, m, dependencies, sprocket_costs = read_file(filename)
    
    # Memoization dictionary
    memo = {}
    
    # Calculate total sprockets for the omnidroid (last part, ID n-1)
    total_cost = calculate_sprockets(n - 1, dependencies, sprocket_costs, memo)
    
    # Output the result
    result = print(f"An omnidroid with {n} parts and {m} dependencies, takes {total_cost} sprockets to build.")
    
    return result

if __name__ == "__main__":
    # This line ensures the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python omnidroid.py <input_file>")
    else:
        # Run the main function with the input file provided as a command-line argument
        main(sys.argv[1])

