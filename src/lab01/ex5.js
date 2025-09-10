const prompt = require('prompt-sync')(); // requires 'npm install prompt-sync'
var a = new Set(prompt('ФИО: ').split(' '));
a.delete('');
var b = Array.from(a);
console.log(`Инициалы: ${b[0][0] + b[1][0] + b[2][0]}.`)
console.log(`Длина (символов): ${b[0].length + b[1].length + b[2].length}.`)