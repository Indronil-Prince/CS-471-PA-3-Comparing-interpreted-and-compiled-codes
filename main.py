import random
import time
import numpy as np

# Function to perform Gaussian elimination without pivoting
def gauss_elim(N):
  for k in range(N-1):
    for i in range(k+1,N):
      pivot = A[k][k]
      factor = A[i][k]/pivot
      A[i][k] = factor
      for j in range(k+1,N+1):
        A[i][j] = A[i][j] - factor*A[k][j]

  # Back substitution
  X = [0.0]*N
  X[N-1] = A[N-1][N]/A[N-1][N-1]
  for i in range(N-2,-1,-1):
    temp = [A[i][j]*X[j] for j in range(i+1,N)]
    X[i] = (A[i][N]-sum(temp))/A[i][i]

  return X



# Main program
if __name__ == '__main__':
  # Read the size of matrix from user input
  N = int(input("Enter the size of the matrix N:"))

  # Initialize the matrix with random numbers
  A = [[random.uniform(0,100) for j in range(N+1)] for i in range(N)]

  # Start the timer
  start = time.time()

  # Perform Gaussian elimination and back substitution
  X = gauss_elim(N)

  # Stop the timer
  finish = time.time()

  # Output the time taken
  print("Time taken for N = ", N, " is ", finish - start, " seconds")
