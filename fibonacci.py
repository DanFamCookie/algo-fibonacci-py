def fibonacci(n):
  # this code is the base case which means if n is 0 or 1 it prints it out because of the fibonacci sequence 
  if n == 0:
    return 0
  elif n == 1:
    return 1

  return fibonacci(n - 1) + fibonacci(n - 2)
#this is the fibonacci sequence 
  pass


print(fibonacci(4))