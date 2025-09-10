const prompt = require('prompt-sync')(); // requires 'npm install prompt-sync'
let a = prompt('Имя: ');
let b = parseInt(prompt('Возраст: '));
console.log(`Привет, ${a}! Через год тебе будет ${b+1}.`);