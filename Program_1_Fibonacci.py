# Define a function to calculate the nth Fibonacci number
def fibonacci(n):
  """
  This function calculates the nth Fibonacci number using recursion.
  - Base cases: 1 and 2 return 1.
  - Recursive case: n is the sum of the (n-1)th and (n-2)th Fibonacci numbers.
  """
  if n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

# Define a function to generate the Fibonacci series up to a given number
def fibonacci_series_up_to_n(n):
  """
  This function generates a list containing all Fibonacci numbers from 1 to n.
  - It iterates through a range from 1 to n (inclusive).
  - For each number, it calculates its Fibonacci value using the fibonacci() function.
  - The calculated value is then appended to a list called "series".
  - Finally, the entire series list containing all Fibonacci numbers up to n is returned.
  """
  series = []
  for i in range(1, n + 1):
    series.append(fibonacci(i))
  return series

# Get the user input for the desired nth position
num = int(input("Enter the value of N: "))

# Validate user input and perform calculations
if num > 0:
  # Calculate the nth Fibonacci number
  fib_value = fibonacci(num)
  # Generate the Fibonacci series up to the given number
  fib_series = fibonacci_series_up_to_n(num)

  # Print the results
  print(f"Fibonacci value at the nth position: {fib_value}")
  print(f"Fibonacci series up to {num}: {fib_series}")
else:
  print("Incorrect value of N.")
