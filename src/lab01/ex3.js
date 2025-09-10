const prompt = require('prompt-sync')(); // requires 'npm install prompt-sync'
var price = parseFloat(prompt());
var discount = parseFloat(prompt());
var vat = parseFloat(prompt());
var base = price * (1 - discount/100);
var vat_amount = base * (vat/100);
var total = base + vat_amount;
console.log(`База после скидки: ${base} ₽`);
console.log(`НДС:               ${vat_amount} ₽`);
console.log(`Итого к оплате:    ${total} ₽`);