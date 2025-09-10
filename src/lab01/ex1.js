const prompt = require('prompt-sync')(); // requires 'npm install prompt-sync'
var a = prompt('Имя: ')
var b = parseInt(prompt('Возраст: '))
console.log('Привет, ${a}! Через год тебе будет ${b+1}.')