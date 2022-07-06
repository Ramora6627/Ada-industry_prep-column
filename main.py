"""
The input to your function will be a tuple of tuples. For example:
((5, 6, 7, 8),
 (3, 9, 2, 5),
 (2, 1, 9, 2))
Your function should return the index of the column with the highest sum.
Examples:
matrix_1 = ((5, 6, 7, 8),
            (3, 9, 2, 5),
            (2, 1, 9, 2))
top_column(matrix_1) => 2
Explanation: Column 2 has a sum of 18, higher than any other column.
matrix_2 = ((1, 2),
            (3, 4))
top_column(matrix_2) => 1
matrix_3 = ((3,),
            (4,),
            (9,))
top_column(matrix_3) => 0
matrix_4 = ((-2, -1, -3),)
top_column(matrix_4) => 1
"""

def top_column(matrix):

  columns = {}
  j = 0
  # print(columns)
  while j < len(matrix[0]):
    for i in range(len(matrix)):
      if j not in columns:
        columns[j] = [matrix[i][j]]
      else:
        columns[j].append(matrix[i][j])
    j += 1
  output = None
  inx = 0
  for key,value in columns.items():
    if output == None or sum(value)>output:
      output = sum(value)
      inx = key
  return inx


# Test cases
matrix_1 = ((5, 6, 7, 8),
            (3, 9, 2, 5),
            (2, 1, 9, 2))
assert top_column(matrix_1) == 2

matrix_2 = ((1, 2),
            (3, 4))
assert top_column(matrix_2) == 1

matrix_3 = ((3,),
            (4,),
            (9,))
assert top_column(matrix_3) == 0

matrix_4 = ((-2, -1, -3),)
assert top_column(matrix_4) == 1

print(top_column(matrix_1))
print("All tests passed!")
print("Finished early? Discuss time & space complexity")


"""
NOTES FOR INTERVIEWER
--------- Clarifying questions ---------------
Q: How should I handle invalid input?
A: You can assume the input will be valid.
Q: Is it possible for different rows to have different numbers of elements?
A: You can assume each row will have the same number of elements.
Q: What should I do if two columns are tied for the highest sum?
A: You can assume there will be no ties.
Q: How should I handle an empty matrix?
A: You can assume the matrix will have at least one element.
--------- Hints -------------------------------
- If your candidate is struggling to form an algorithm, encourage them to explain how they would do it by hand. If they are still unsure, help them to realize that they will need to iterate over the column indices in the outer loop, and the row indices in the inner loop.
- If your candidate forgets to reset their sum for each column, encourage them to print out the total for each column.
"""