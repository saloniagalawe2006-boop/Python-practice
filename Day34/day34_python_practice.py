"""
🐍 Day 34: Recursion
"""

# ----------------------------------------------------
# 1. What is Recursion?
# ----------------------------------------------------
# A recursive function is a function that calls ITSELF
# to solve smaller versions of the same problem.
# Every recursive function needs:
#   1. A BASE CASE (stopping condition)
#   2. A RECURSIVE CASE (calls itself with a smaller input)


# ----------------------------------------------------
# 2. Classic example: Factorial
# ----------------------------------------------------
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    if n == 0 or n == 1:      # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))


# ----------------------------------------------------
# 3. Comparing with the loop-based (iterative) way
# ----------------------------------------------------

def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\nFactorial (loop version) of 6:", factorial_loop(6))
print("Factorial (recursive version) of 6:", factorial(6))


# ----------------------------------------------------
# 4. Fibonacci sequence using recursion
# ----------------------------------------------------
# 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(n):
    if n <= 1:                # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # recursive case

print("\nFirst 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()


# ----------------------------------------------------
# 5. Sum of a list using recursion
# ----------------------------------------------------

def recursive_sum(numbers):
    if len(numbers) == 0:     # base case
        return 0
    return numbers[0] + recursive_sum(numbers[1:])   # recursive case

nums = [1, 2, 3, 4, 5]
print("\nSum of", nums, "=", recursive_sum(nums))


# ----------------------------------------------------
# 6. Countdown using recursion
# ----------------------------------------------------

def countdown(n):
    if n <= 0:                # base case
        print("Liftoff! 🚀")
        return
    print(n)
    countdown(n - 1)           # recursive case

print("\n--- Countdown ---")
countdown(5)


# ----------------------------------------------------
# 7. Reverse a string using recursion
# ----------------------------------------------------

def reverse_string(s):
    if len(s) == 0:            # base case
        return s
    return reverse_string(s[1:]) + s[0]   # recursive case

print("\nReversed 'python':", reverse_string("python"))


# ----------------------------------------------------
# 8. What happens WITHOUT a base case (danger!)
# ----------------------------------------------------
# def broken_recursion(n):
#     return broken_recursion(n - 1)   # NO base case -> infinite recursion
#     -> causes RecursionError: maximum recursion depth exceeded
# (kept commented out on purpose — do not run this)


"""
📝 Quick Recap:
- Recursion = a function calling itself
- MUST have a base case, or it runs forever (RecursionError)
- Each call works on a SMALLER version of the problem
- Useful for: factorial, Fibonacci, tree/folder structures,
  sum of lists, reversing strings, divide-and-conquer algorithms
- Recursion is elegant but can be slower/more memory-heavy than
  loops for simple problems — use it when it makes the logic clearer
"""