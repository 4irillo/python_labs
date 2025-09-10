const prompt = require('prompt-sync')(); // requires 'npm install prompt-sync'
var t = parseInt(prompt('Минуты: '));
if (t%60>9)
{
    var m = t%60
}
else
{
    var m = '0' + t%60
}
console.log(`${parseInt(t/60)}:${m}`)