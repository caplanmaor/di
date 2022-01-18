// exercise 1

function infoAboutMe() {
  console.log("name maor age 26 hobbies mountainbiking");
}

function infoAboutPerson(personName, personAge, personFavoriteColor) {
  console.log(
    `your name is ${personName} you are ${personAge} years old and your favorite color is ${personFavoriteColor}`
  );
}

infoAboutPerson("Michael Jackson", "160", "grey");
infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

// exercise 2

let input = 150;

const calculateTip = () => {
  if (input < 50) {
    tip = 20;
  } else if (input < 200) {
    tip = 15;
  } else {
    tip = 10;
  }
  console.log(
    `the bill is ${input}$ so you should tip ${input * (tip / 100)} `
  );
};

calculateTip();

// exercise 3

function isDivisible() {
  let numbers = [];
  for (let i = 0; i < 500; i++) {
    if (i % 23 == 0) {
      numbers.push(i);
    }
  }
  console.log(numbers);
}

isDivisible();

// exercise 4

let stock = {
  banana: 6,
  apple: 0,
  pear: 12,
  orange: 32,
  blueberry: 1,
};

let prices = {
  banana: 4,
  apple: 2,
  pear: 1,
  orange: 1.5,
  blueberry: 10,
};

let shoppingList = ["banana", "orange", "apple"];

function myBill() {
  let totalPrice = 0;
  shoppingList.forEach((listElement) => {
    for (let key of Object.keys(stock)) {
      if (listElement == key) {
        totalPrice += stock[key];
      }
    }
  });
  return totalPrice;
}

console.log(myBill());

// exercise 5

function changeEnough(itemPrice, amountOfChange) {
  let quarter = amountOfChange[0] * 0.25;
  let dime = amountOfChange[1] * 0.1;
  let nickel = amountOfChange[2] * 0.05;
  let penny = amountOfChange[3] * 0.01;
  let totalChange = quarter + dime + nickel + penny;
  console.log(totalChange);
  if (totalChange >= itemPrice) {
    return true;
  } else {
    return false;
  }
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));

// exercise 6

function hotelCost() {
  let input = "";
  while (input == "" || isNaN(input) == true) {
    input = window.prompt("how many nights in a hotel?");
  }
  return input * 140;
}

function planeRideCost() {
  let input = "";
  while (input == "" || isNaN(input) == false) {
    input = window.prompt("where do you fly?");
  }
  if (input == "london") {
    return 183;
  } else if (input == "paris") {
    return 220;
  } else {
    return 300;
  }
}

function rentalCarCost() {
  let input = "";
  while (input == "" || isNaN(input) == true) {
    input = window.prompt("number of days you need a car?");
  }
  if (input > 10) {
    return 40 * input * 0.95;
  } else {
    return 40 * input;
  }
}

function totalVacationCost() {
  return hotelCost() + planeRideCost() + rentalCarCost();
}

console.log(totalVacationCost());
