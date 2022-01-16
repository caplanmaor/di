// exercise 1
let people = ["Greg", "Mary", "Devon", "James"];

people.shift();

// Write code to remove “Greg” from the people array.
console.log(people);

// Write code to replace “James” to “Jason”.
people[2] = people[2].replace("James", "Jason");
console.log(people);

// Write code to add your name to the end of the people array.

people.push("Maor");
console.log(people);

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
console.log(people.indexOf("Mary"));

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

let slicedPeople = people.slice(1, 3);
console.log(slicedPeople);

// Write code that gives the index of “Foo”. Why does it return -1 ?
console.log(people.indexOf("Foo")); // returns -1 because its not in the array

// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?

let last = people[people.length - 1];
console.log("the last person is: " + last);
// length - 1 is the last item in the array

// Using a loop, iterate through the people array and console.log each person.
for (let person of people) {
  console.log(person);
}

// Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
for (let person of people) {
  console.log(person);
  if (person == "Jason") {
    break;
  }
}

// exercise 2
// Create an array called colors where the value is a list of your five favorite colors.
let colors = ["blue", "purple", "black", "red"];

// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
for (let i = 0; i < colors.length; i++) {
  console.log(`my #${i + 1} choice is ${colors[i]}`);
}

// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

let suffixes = ["st", "nd", "rd", "th"];
for (let i = 0; i < colors.length; i++) {
  console.log(`my ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}

// exercise 3
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
let input = 0;
while (input < 10) {
  input = prompt("choose a number");
  console.log("your input is as a " + typeof input);
}

// exercise 4
// Copy and paste this object to your Javascript file.
let building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

// Console.log the number of floors in the building.
console.log(building.numberOfFloors);

// Console.log how many apartments are on the floors 1 and 3.
console.log(
  `on the first floor there is ${building.numberOfAptByFloor.firstFloor} and on the third floor there is ${building.numberOfAptByFloor.thirdFloor}`
);

// Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log(
  `the second tenet is ${building.nameOfTenants[1]} he has ${building.numberOfRoomsAndRent.dan[0]} rooms in his apartment`
);

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
if (
  building.numberOfRoomsAndRent.sarah[1] +
    building.numberOfRoomsAndRent.david[1] >
  building.numberOfRoomsAndRent.dan[1]
) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
}

// exercise 5
// Create an object called family with a few key value pairs.
let family = {
  maor: "father",
  zohar: "mother",
  pazit: "daughter",
};

// Using a for loop, console.log the keys of the object.
for (let member in family) {
  console.log(member);
}

// Using a for loop, console.log the values of the object.
for (let role in family) {
  console.log(family[role]);
}

// exercise 6
// Given the object and using a for loop, console.log “my name is Rudolf the raindeer”
let details = {
  my: "name",
  is: "Rudolf",
  the: "raindeer",
};

let sentance = "";
for (let detail in details) {
  sentance += detail + " ";
  sentance += details[detail] + " ";
}
console.log(sentance);

// exercise 7
// A group of friends have decided to start a secret society.
// The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let secretName = [];
for (let name of names) {
  secretName.push(name[0]);
}
secretName.sort();
console.log(secretName.join(""));
