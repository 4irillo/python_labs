const prompt = require('prompt-sync')(); // requires 'npm install prompt-sync'
var str = prompt();
var ans = "";
var flag1 = false;
var flag2 = false;
var start = 0;
var step = 0;
for (var i = 0; i < str.length; i++)
{
    var currChar = str[i];
    if (!flag1 &&currChar === currChar.toLocaleUpperCase() && (currChar > '9' || currChar < '0') && currChar !== '.')
    {
        flag1 = true;
        start = i;
    }
    if (!flag2 && flag1 && currChar <= '9' && currChar >= '0')
    {
        flag2 = true;
        step = i - start + 1;
        console.log(step);
    }
        
}
var k = 0;
while (str[start + k * step] !== '.')
{
    ans += str[start + k * step];
    k+=1;
}
/*console.log('Start char: ' + str[start]);
console.log('Start ind:  ' + start);
console.log('Step:       ' + step);
console.log('Next symb:  ' + str[start+step]);
*/



console.log(ans)

// node src/lab01/ex7.js
// thisisabracadabraHt1eadljjl12ojh.



/*var char = str[i]
    if (!flag1 && char === char.toUpperCase())
    {
        ans += char;
        flag1 = true;
        var step = 0;
        var start = i;
    }
    if (flag1 && '0' > char && char > '9')
    {
        step+=1;
        ans += str[i+1];
    }
    if (flag1 && char <= '9' && char >= '0')
    {
        for (var j = 1; j< str.length - start; j++)
        {
            try{ans += str[start + step * j];}
            catch(error) {break;}
            finally{console.log(ans);}

        }
    }
    if (char === '.')
    {
        break;
    }*/