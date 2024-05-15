#!/usr/bin/python3
"""A method that calculates the fewest number of operations needed to result in exactly n H characters in the file"""

def minOperations(n):
    # If n is 0 or 1, it's impossible to obtain 'H'
    if n <= 1:
        return n
    
    # Initialize a list to store minimum operations for each number
    dp = [float('inf')] * (n + 1)
    
    # It takes 0 operations to reach 1 'H'
    dp[1] = 0
    
    # Iterate through each number from 2 to n
    for i in range(2, n + 1):
        # Check all possible divisors of i
        for j in range(1, i):
            # If i is divisible by j
            if i % j == 0:
                # Update minimum operations for i if needed
                dp[i] = min(dp[i], dp[j] + i // j)
    
    # Return the minimum operations needed for n characters
    return dp[n] if dp[n] != float('inf') else 0

# Test cases
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
