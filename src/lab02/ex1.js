import prompt from 'prompt-sync'// requires 'npm install prompt-sync'
import * as tuple from '../libs/tuples.js';
import * as arrays from '../libs/arrays.js';
import * as matrixes from '../libs/matrixes.js';

//Arrays
//min_max
console.log("min_max");
console.log(`input: [3, -1, 5, 5, 0],  output: ${arrays.min_max([3, -1, 5, 5, 0])}`);
console.log(`input: [42],  output: ${arrays.min_max([42])}`);
console.log(`input: [-5, -2, -9],  output: ${arrays.min_max([-5, -2, -9])}`);
//console.log(arrays.min_max([])); -- error test
console.log(`input: [1.5, 2, 2.0, -3.1],  output: ${arrays.min_max([1.5, 2, 2.0, -3.1])}`);
//unique_sorted
console.log("unique_sorted")
console.log(`input: [3, 1, 2, 1, 3],  output: ${arrays.unique_sorted([3, 1, 2, 1, 3])}`);
console.log(`input: [],  output: ${arrays.unique_sorted([])}`);
console.log(`input: [-1, -1, 0, 2, 2],  output: ${arrays.unique_sorted([-1, -1, 0, 2, 2])}`);
console.log(`input: [1.0, 1, 2.5, 2.5, 0],  output: ${arrays.unique_sorted([1.0, 1, 2.5, 2.5, 0])}`);
//flatten
console.log("flatten");
console.log(`input: [[1, 2], [3, 4]],  output: ${arrays.flatten([[1, 2], [3, 4]])}`);
//console.log(([1, 2], (3, 4, 5))) в жс нет кортежей, но если бы были, то это Object.seal(array), который мой код хавает нормас
console.log(`input: [[1], [], [2, 3]],  output: ${arrays.flatten([[1], [], [2, 3]])}`);
//console.log(arrays.flatten([[1, 2], "ab"])); -- error test
console.log("\n");

//Matrixes
//transpose
console.log("transpose");
console.log(`input: [[1, 2, 3]],  output: ${matrixes.transpose([[1, 2, 3]])}`);
console.log(`input: [[1], [2], [3]],  output: ${matrixes.transpose([[1], [2], [3]])}`);
console.log(`input: [[1, 2], [3, 4]],  output: ${matrixes.transpose([[1, 2], [3, 4]])}`);
console.log(`input: [],  output: ${matrixes.transpose([])}`);
//console.log(matrixes.transpose([[1, 2], [3]])); -- error test
//row_sums
console.log("row_sums");
console.log(`input: [[1, 2, 3], [4, 5, 6]],  output: ${matrixes.row_sums([[1, 2, 3], [4, 5, 6]])}`);
console.log(`input: [[-1, 1], [10, -10]],  output: ${matrixes.row_sums([[-1, 1], [10, -10]])}`);
console.log(`input: [[0, 0], [0, 0]],  output: ${matrixes.row_sums([[0, 0], [0, 0]])}`);
//console.log(matrixes.row_sums([[1, 2], [3]])); -- error test
//col_sums
console.log("col_sums");
console.log(`input: [[1, 2, 3], [4, 5, 6]],  output: ${matrixes.col_sums([[1, 2, 3], [4, 5, 6]])}`);
console.log(`input: [[-1, 1], [10, -10]],  output: ${matrixes.col_sums([[-1, 1], [10, -10]])}`);
console.log(`input: [[0, 0], [0, 0]],  output: ${matrixes.col_sums([[0, 0], [0, 0]])}`);
//console.log(matrixes.col_sums([[1, 2], [3]])); -- error test
console.log("\n");

//Tuples
console.log("tuples")
console.log(`input: ("Иванов Иван Иванович", "BIVT-25", 4.6),  output: ${new tuple.Tuple("Иванов Иван Иванович", "BIVT-25", 4.6).format_record()}`);
console.log(`input: ("Петров Пётр", "IKBO-12", 5.0),  output: ${new tuple.Tuple("Петров Пётр", "IKBO-12", 5.0).format_record()}`);
console.log(`input: ("Петров Пётр Петрович", "IKBO-12", 5.0),  output: ${new tuple.Tuple("Петров Пётр Петрович", "IKBO-12", 5.0).format_record()}`);
console.log(`input: ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),  output: ${new tuple.Tuple("  сидорова  анна   сергеевна ", "ABB-01", 3.999).format_record()}`);