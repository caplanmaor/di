const gameInfo = [
  {
    username: "john",
    team: "red",
    score: 5,
    items: ["ball", "book", "pen"],
  },
  {
    username: "becky",
    team: "blue",
    score: 10,
    items: ["tape", "backpack", "pen"],
  },
  {
    username: "susy",
    team: "red",
    score: 55,
    items: ["ball", "eraser", "pen"],
  },
  {
    username: "tyson",
    team: "green",
    score: 1,
    items: ["book", "pen"],
  },
];

let userNames = gameInfo.map((e) => e.username + "!");
document.body.textContent += userNames;

let redTeam = gameInfo.filter((e) => e.team.includes("red"));
console.log(redTeam);

////////////////////////

const data = [
  {
    name: "Butters",
    age: 3,
    type: "dog",
  },
  {
    name: "Cuty",
    age: 5,
    type: "rabbit",
  },
  {
    name: "Lizzy",
    age: 6,
    type: "dog",
  },
  {
    name: "Red",
    age: 1,
    type: "cat",
  },
  {
    name: "Joey",
    age: 3,
    type: "dog",
  },
  {
    name: "Rex",
    age: 10,
    type: "dog",
  },
];

// let sumYears = 0;
// data.forEach((element) => {
//   sumYears += element.age;
// });

// let sumYearsMap = data.map((e) => e.age);

// console.log(sumYearsMap);
sumReduce = data.reduce((acc, e) => {
  return acc + e.age;
}, 0);
console.log(sumReduce * 7);
