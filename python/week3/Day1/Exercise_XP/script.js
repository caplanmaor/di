// exercise 1

let favFood = "steak";
let favMeal = "breakfest";
console.log(`i eat ${favFood} for ${favMeal} every morning`);

// exercise 2

let watchedSeries = ["black mirror", "money heist", "the big bang theory"];
let arrLength = watchedSeries.length;
let sentence = "i watched: ";
console.log(sentence + watchedSeries);

watchedSeries[3] = "friends";
watchedSeries.push("the sopranos");
watchedSeries.unshift("Evangelion");
watchedSeries.splice(1, 1);
console.log(watchedSeries[1][2]);
console.log(watchedSeries);

// exercise 3

let temp = 25;
let convertedTemp = (temp / 5) * 9 + 32;
console.log(`${temp}°C is ${convertedTemp}°F`);

// exercise 4
let c;
let a = 34;
let b = 21;

console.log(a + b); //first expression
// Prediction: 55
// Actual: 55

a = 2;

console.log(a + b); //second expression
// Prediction: 23
// Actual: 23

// value of c is undefined
// console.log(3 + 4 + "5"); should be 75 because the string gets added literally to the end of the line

//exercise 5

typeof 15;
// Prediction: int
// Actual: number
//i think it will be an int because its a whole number

typeof 5.5;
// Prediction: float
// Actual: number
// float because it has a decimal point

typeof NaN;
// Prediction: undefined
// Actual: number
// i thought undefined but nan is a number

typeof "hello";
// Prediction: string
// Actual:string
//because its a stirng of letters

typeof true;
// Prediction: boleans
// Actual: bolean
//because its true or false

typeof (1 != 2);
// Prediction: bolean
// Actual: bolean
// bolean because its a conditional

"hamburger" + "s";
// Prediction: string
// Actual: string
//string

"hamburgers" - "s";
// Prediction: string
// Actual: NaN
//string hamburger but i guess you cant do string - string

"1" + "3";
// Prediction: string
// Actual: string
//because of the ""

"1" - "3";
// Prediction: NaN
// Actual: number
//i thought it wouldnt work but it did become a number -2

"johnny" + 5;
// Prediction: NaN
// Actual: string
//i thought it wont work but it did

"johnny" - 5;
// Prediction: NaN
// Actual: number
//because nan is a number type

99 * "hello";
// Prediction: number
// Actual: number
// because nan is a number type

1 != 1;
// Prediction: bloean
// Actual: bloean
// bolean because its a conditional

1 == "1";
// Prediction: bloean
// Actual: bloean
// bolean because its a conditional

1 === "1";
// Prediction: bloean
// Actual: bloean
// bolean because its a conditional

// exercise 6

5 + "34";
// Prediction: string
// Actual: string
// because a string cant be converted to a number with +

5 - "4";
// Prediction: number
// Actual: number
// because NaN is considered a number type

10 % 5;
// Prediction: number
// Actual: number
// because its a mathematical operation

5 % 10;
// Prediction: number
// Actual: number
// because its a mathematical operation

"Java" + "Script";
// Prediction: string
// Actual: string
// because its two strings

" " + " ";
// Prediction: string
// Actual: string
// because its two strings

" " + 0;
// Prediction: string
// Actual: string
// the number gets converted to a string

true + true;
// Prediction: bolean
// Actual: number
// because true is 1

true + false;
// Prediction: number
// Actual: number
// because its like 1 + 0

false + true;
// Prediction: number
// Actual: number
// because its like 0 + 1

false - true;
// Prediction: number
// Actual: number
// because its like 0 - 1

!true;
// Prediction: boolean
// Actual: bolean
// because its false

3 - 4;
// Prediction: number
// Actual: number
// because 1 is a number

"Bob" - "bill";
// Prediction: number
// Actual: number
// because its NaN which is a number type
