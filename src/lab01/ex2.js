const prompt = require('prompt-sync')(); // requires 'npm install prompt-sync'
var a = parseInt(prompt('a: '));
var b = parseInt(prompt('bck: '));
console.log(`sum=${a+b}; avg=${(a+b)/2}`)