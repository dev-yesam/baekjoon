n = int(input())
arr = list(map(int, input().split()))

# Sort the array first
arr.sort()

# Start with 1 as the smallest natural number
smallest = 1

# Iterate through the array
for num in arr:
    # If the current number is greater than the smallest
    # That means we cannot form the number 'smallest'
    if num > smallest:
        break
    smallest += num

# The 'smallest' is the smallest number that cannot be formed by the sum of subsets of the array
print(smallest)
