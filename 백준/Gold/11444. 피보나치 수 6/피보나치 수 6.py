import sys

input = sys.stdin.readline

MOD = 1000000007

def matrix_multiply(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            for k in range(n):
                result[row][col] += A[row][k] * B[k][col]
                result[row][col] %= MOD
    return result

def matrix_power(A, k):
    if k == 1:
        for row in range(len(A)):
            for col in range(len(A)):
                A[row][col] %= MOD
        return A
    
    half_power = matrix_power(A, k//2)
    if k % 2 == 1:
        return matrix_multiply(matrix_multiply(half_power, half_power), A)
    else:
        return matrix_multiply(half_power, half_power)

n = int(input())

fib_matrix = [[1, 1], [1, 0]]

print(matrix_power(fib_matrix, n)[0][1])