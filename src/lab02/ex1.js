import prompt from 'prompt-sync'// requires 'npm install prompt-sync'
import * as tuple from '../libs/tuples.js';
//console.log(typeof([3, -1, 5, 5, 0]))
let a = new tuple.Tuple("  сидорова  анна   сергеевна ", "ABB-01", 3.407)
console.log(a.getData());