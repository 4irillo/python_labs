const prompt = require('prompt-sync')(); // requires 'npm install prompt-sync'
var a = parseInt(prompt('a: '));
var b = parseInt(prompt('b: '));
console.log(`sum=${a+b}; avg=${(a+b)/2}`)