# ayushiawasthi
Assignmentq
m=int(input("Row:"))
n=int(input("Column:"))
matrix=[[0 for col in range(n)] for row in range(m)]
for row in range(m):
  for column in range(n):
    matrix[row][column]=row*column
print(matrix)    
