const prompt = require('prompt-sync')(); // requires 'npm install prompt-sync'

class Person {
    constructor([name, secondName, age, format])
    {
        this.name = name;
        this.secondName = secondName;
        this.age = parseInt(age);
        this.format = format.toLowerCase() === 'true';
    }

};

var n = parseInt(prompt());
var dist = 0;
var real = 0;
for (var i = 0; i < n; i++)
{
    var person = new Person(prompt().split(' '));
    if (person.format === true)
    {
        real++;
    }
    else
    {
        dist++;
    }
}
console.log(real +' '+ dist)