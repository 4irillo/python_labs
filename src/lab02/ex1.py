import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from libs.arrays import flatten
from libs.arrays import min_max
from libs.arrays import unique_sorted
from libs.matrixes import transpose
from libs.matrixes import row_sums
from libs.matrixes import col_sums
from libs.tuples import Tuple
from libs.tuples import format_record

# Arrays
# min_max
print("min_max")
print(f"input: [3, -1, 5, 5, 0],  output: {min_max([3, -1, 5, 5, 0])}")
print(f"input: [42],  output: {min_max([42])}")
print(f"input: [-5, -2, -9],  output: {min_max([-5, -2, -9])}")
#print(min_max([])) #-- error test
print(f"input: [1.5, 2, 2.0, -3.1],  output: {min_max([1.5, 2, 2.0, -3.1])}")
# unique_sorted
print("unique_sorted")
print(f"input: [3, 1, 2, 1, 3],  output: {unique_sorted([3, 1, 2, 1, 3])}")
print(f"input: [],  output: {unique_sorted([])}")
print(f"input: [-1, -1, 0, 2, 2],  output: {unique_sorted([-1, -1, 0, 2, 2])}")
print(f"input: [1.0, 1, 2.5, 2.5, 0],  output: {unique_sorted([1.0, 1, 2.5, 2.5, 0])}")
# flatten
print("flatten")
print(f"input: [[1, 2], [3, 4]],  output: {flatten([[1, 2], [3, 4]])}")
# print(arrays.flatten([[1, 2], "ab"])) -- error test
print(f"input: [[1], [], [2, 3]],  output: {flatten([[1], [], [2, 3]])}")
print("\n")

# Matrixes
# transpose
print("transpose")
print(f"input: [[1, 2, 3]],  output: {transpose([[1, 2, 3]])}")
print(f"input: [[1], [2], [3]],  output: {transpose([[1], [2], [3]])}")
print(f"input: [[1, 2], [3, 4]],  output: {transpose([[1, 2], [3, 4]])}")
print(f"input: [],  output: {transpose([])}")
# print(matrixes.transpose([[1, 2], [3]])) -- error test
# row_sums
print("row_sums")
print(f"input: [[1, 2, 3], [4, 5, 6]],  output: {row_sums([[1, 2, 3], [4, 5, 6]])}")
print(f"input: [[-1, 1], [10, -10]],  output: {row_sums([[-1, 1], [10, -10]])}")
print(f"input: [[0, 0], [0, 0]],  output: {row_sums([[0, 0], [0, 0]])}")
# print(matrixes.row_sums([[1, 2], [3]])) -- error test
# col_sums
print("col_sums")
print(f"input: [[1, 2, 3], [4, 5, 6]],  output: {col_sums([[1, 2, 3], [4, 5, 6]])}")
print(f"input: [[-1, 1], [10, -10]],  output: {col_sums([[-1, 1], [10, -10]])}")
print(f"input: [[0, 0], [0, 0]],  output: {col_sums([[0, 0], [0, 0]])}")
# print(matrixes.col_sums([[1, 2], [3]])) -- error test
print("\n")

# Tuples
print("tuples")
a = Tuple("Иванов Иван Иванович", "BIVT-25", 4.6).format_record()
print(f"input: (Иванов Иван Иванович, BIVT-25, 4.6),  output: {a}")
a = Tuple("Петров Пётр", "IKBO-12", 5.0).format_record()
print(f"input: (Петров Пётр, IKBO-12, 5.0),  output: {a}")
a = Tuple("Петров Пётр Петрович", "IKBO-12", 5.0).format_record()
print(f"input: (Петров Пётр Петрович, IKBO-12, 5.0),  output: {a}")
a = Tuple("  сидорова  анна   сергеевна ", "ABB-01", 3.999).format_record()
print(f"input: (  сидорова  анна   сергеевна , ABB-01, 3.999),  output: {a}")

#Tuples 2.0
print("tuples 2.0 ")
a = format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))
print(f"input: (Иванов Иван Иванович, BIVT-25, 4.6),  output: {a}")
a = format_record(("Петров Пётр", "IKBO-12", 5.0))
print(f"input: (Петров Пётр, IKBO-12, 5.0),  output: {a}")
a = format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))
print(f"input: (Петров Пётр Петрович, IKBO-12, 5.0),  output: {a}")
a = format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))
print(f"input: (  сидорова  анна   сергеевна , ABB-01, 3.999),  output: {a}")

#test commit