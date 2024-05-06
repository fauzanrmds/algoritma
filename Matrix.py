def pengurangan(matrix):
  n = len(matrix)
  diagonal1 = 0
  diagonal2 = 0

  for i in range(n):
    diagonal1 += matrix[i][i]
    diagonal2 += matrix[n - 1 - i][i]

  return diagonal1 - diagonal2

Matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]

hasil = pengurangan(Matrix)
print(f"Hasil: {hasil}")