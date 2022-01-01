// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ["bread", ...vegetables, "chicken", ...fruits];
// console.log(result);

// const country = "USA";
// console.log([...country]);

// let newArray = [...[, ,]];
// console.log(newArray);

/////////////////////////////////////////////////

// let users = [
//   { firstName: "Bradley", lastName: "Bouley", role: "Full Stack Resident" },
//   { firstName: "Chloe", lastName: "Alnaji", role: "Full Stack Resident" },
//   { firstName: "Jonathan", lastName: "Baughn", role: "Enterprise Instructor" },
//   { firstName: "Michael", lastName: "Herman", role: "Lead Instructor" },
//   { firstName: "Robert", lastName: "Hajek", role: "Full Stack Resident" },
//   { firstName: "Wes", lastName: "Reid", role: "Instructor" },
//   { firstName: "Zach", lastName: "Klabunde", role: "Instructor" },
// ];

//say hello to everyone
// let greete = users.map((e) => {
//   return "hello " + e.firstName;
// });

// console.log(greete);

// say hello only to Full Stack Residents

// let fsResidents = users
//   .filter((e) => e.role === "Full Stack Resident")
//   .map((e) => "hello " + e.firstName);

// console.log(fsResidents);

///////////////////////////////////////////////////

let epicWords = [
  "a",
  "long",
  "time",
  "ago",
  "in a",
  "galaxy",
  "far far",
  "away",
];

let epicSentance = epicWords.reduce((accum, e) => (accum += e + " "));

document.body.textContent += epicSentance;

/////////////////////////////////////////////////

let students = [
  { name: "Ray", course: "Computer Science", isPassed: true },
  { name: "Liam", course: "Computer Science", isPassed: false },
  { name: "Jenner", course: "Information Technology", isPassed: true },
  { name: "Marco", course: "Robotics", isPassed: true },
  { name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
  { name: "Jamie", course: "Big Data", isPassed: false },
];

let studentsPassed = students
  .filter((e) => e.isPassed === true)
  .map((e) => e.name + " you passed the course: " + e.course);
// console.log(studentsPassed);

// const arrayNum = [1, 2, 4, 5, 8, 9];
// const newArray = arrayNum.map((num, i) => {
//   console.log(num, i);
//   alert(num);
//   return num * 2;
// });

const array = [[1], [2], [3], [[[4]]], [[[5]]]];
let concatedArray = array.reduce((acc, e) => acc.concat(e));
console.log(concatedArray);

/////////////////////////////////////////////

//GOLD XP

const greeting = [
  ["Hello", "young", "grasshopper!"],
  ["you", "are"],
  ["learning", "fast!"],
];

greeting.forEach((element) => {
  element = element.join(" ");
});
// console.log(greeting2);
console.log(greeting);

greeting2 = greeting.reduce((acc, e) => acc.concat(e));
console.log(greeting2.join(" "));

const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]];
console.log(trapped);

////////////////////////////////////////////

//Daily Challenge

let inventory = [
  { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
  { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
  { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
  {
    id: 4,
    car_make: "Land Rover",
    car_model: "Defender Ice Edition",
    car_year: 2010,
  },
  { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

function getCarHonda(carInventory) {
  let firstHonda = inventory.find((e) => e.car_make == "Honda");
  return `This is a ${firstHonda.car_make} ${firstHonda.car_model} from ${firstHonda.car_year}`;
}
console.log(getCarHonda());

//////////////////////////////////////

function sortCarInventoryByYear(carInventory) {
  sortedInventory = inventory.sort((x, y) => {
    return x.car_year - y.car_year;
  });
  return sortedInventory;
}

console.log(sortCarInventoryByYear());
