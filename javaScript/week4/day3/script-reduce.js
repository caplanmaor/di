const students = [
  { name: "Rich", score: 33 },
  { name: "Peter", score: 55 },
  { name: "John", score: 75 },
];

let sum = students.reduce((accum, e) => {
  return accum + e.score;
}, 0);

// document.body.textContent = sum;

///////////////////////////////////

let voters = [
  { name: "Bob", age: 30, voted: true },
  { name: "Jake", age: 32, voted: true },
  { name: "Kate", age: 25, voted: false },
  { name: "Sam", age: 20, voted: false },
  { name: "Bob", age: 30, voted: true },
];

let numberOfVoters = voters.reduce((accum, e) => {
  return accum + e.voted;
}, 0);

document.body.textContent += numberOfVoters;
