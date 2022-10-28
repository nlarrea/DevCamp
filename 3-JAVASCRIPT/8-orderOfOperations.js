// ORDER OF OPERATIONS
/*
PEMDAS
Parenthesis - Exponents - Multiplication - Division - Addition - Substraction
*/
var num = 5 + 5 * 10;
console.log(num); // 55 -> 5 * 10 = 50 -> 50 + 5 = 55

var num2 = 5 + (5 * 10) / 6**2 -1;
console.log(num2); // 5.388888888889
/* 5 * 10 = 50 -> 6**2 -> 50 / 36 = 1.388888888 -> 5 + 1.38888 = 6.3888888 -> 6.38888 - 1 = 5.3888888 */