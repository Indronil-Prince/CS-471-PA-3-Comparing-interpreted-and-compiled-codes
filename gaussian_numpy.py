import random
import time
import numpy as np

def gaussian_elimination_numpy(N):
    # Perform Gaussian elimination with back substitution
    A = np.random.rand(N, N+1)
    for k in range(N):
        for i in range(k+1, N):
            factor = A[i,k] / A[k,k]
            A[i,k:N+1] -= factor * A[k,k:N+1]
    
    x = np.zeros(N)
    x[N-1] = A[N-1,N] / A[N-1,N-1]
    for i in range(N-2, -1, -1):
        x[i] = (A[i,N] - np.dot(A[i,i+1:N], x[i+1:N])) / A[i,i]
    
    return x

# Main program
if __name__ == '__main__':
  # Read the size of matrix from user input
  N = int(input("Enter the size of the matrix N:"))
  start = time.time()
  X = gaussian_elimination_numpy(N)
  finish = time.time()

  # Output the time taken
  print("Time taken for N = ", N, " is ", finish - start, " seconds")

