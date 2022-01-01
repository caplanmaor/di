// const studentsFootball = [
//   { name: "Rich", score: 33 },
//   { name: "Peter", score: 55 },
// ];

// let studentsAvarage = studentsFootball.map((e, i, a) => {
//   let isAboveAverage = e.score > 50 ? true : false;
//   return {
//     name: e.name,
//     score: e.score,
//     isAboveAverage,
//   };
// });

// console.log(studentsAvarage);

///////////////////////////////////////////////////////////////

// let famousPeople = [
//   {
//     name: "Angelina Jolie",
//     job: "actor",
//     age: 80,
//   },
//   {
//     name: "Georges Clooney",
//     job: "actor",
//     age: 2,
//   },
//   {
//     name: "Paris Hilton",
//     job: "actor",
//     age: 5,
//   },
//   {
//     name: "Kayne West",
//     job: "singer",
//     age: 16,
//   },
//   {
//     name: "Britney Spears",
//     job: "singer",
//     age: 100,
//   },
// ];
// 1. Use the map method, to create a new array and push the name of the people which age
// is equal or bigger than 16.
// 2. Use the map method, to create a new array and to push an object in the new array.
// Each object should contain the name of the actor, and it's job
// 3. BONUS: Use for each to add each of thoses names on the DOM (in a paragraph, appended to a div with an id "container")
// let famousAdults = famousPeople.map((e) => {
//   let nameAndJob = e.name + " " + e.job;
//   return {
//     name: e.name,
//     job: e.job,
//     age: e.age,
//     nameAndJob,
//   };
// });

// famousAdults.forEach((e) => {
//   let container = document.getElementById("container");
//   let person = document.createTextNode(e.nameAndJob);
//   container.appendChild(person);
//   container.appendChild(document.createElement("br"));
// });

/////////////////////////////////////////////////////////////////

// const students = [
//   { name: "maor", score: 33 },
//   { name: "nadav", score: 98 },
//   { name: "dor", score: 77 },
// ];

// let bestStudents = students.filter((e) => e.score > 50);
// console.log(bestStudents);

/////////////////////////////////////////////////////////

//Exercise 1:  create a new array that filters only the positive value
let numbers = [-23, -20, -17, -12, -5, 0, 1, 5, 12, 19, 20];

let positiveNumbers = numbers.filter((e) => e > 0);
document.body.textContent += positiveNumbers;

// Exercise 2: Suppose you have a list of Star Trek characters,
// and you want to get just the characters that appeared in Star Trek: The Next Generation.
// Use filter() to filter the array of characters below
const characters = [
  { name: "James T. Kirk", series: ["Star Trek"] },
  { name: "Spock", series: ["Star Trek", "Star Trek: The Next Generation"] },
  { name: "Jean-Luc Picard", series: ["Star Trek: The Next Generation"] },
  {
    name: "Worf",
    series: ["Star Trek: The Next Generation", "Star Trek: Deep Space Nine"],
  },
];

let newCharacters = characters
  .filter((e) => e.series.includes("Star Trek: The Next Generation"))
  .map((e) => e.name);
console.log(newCharacters);

////////////////////////////////////////////////////////

const colors = ["blue", "red", "blue", "yellow"];
// let uniqueColors = [...new Set(colors)];
// console.log(uniqueColors);
colors.forEach((e) => {
  //do something
});
