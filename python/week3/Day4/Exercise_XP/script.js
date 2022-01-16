// exercise 1
// Create 2 variables, x and y. Each of them should have a different numeric value.
// Write an if/else statement that checks which number is bigger.

let x = 5;
let y = 2;

if (x > y) {
  console.log("x is bigger");
} else {
  console.log("y is bigger");
}

// exercise 2
// 1. Create a variable called newDog where it’s value is “Chihuahua”.
let newDog = "Chihuahua";

// 2. Check and display how many letters are in newDog.
let length = newDog.length;
console.log(length);

// 3. Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

// 4. Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’

newDog = "Chihuahua"
  ? console.log("i love chihuahuas its my favorite dog breed")
  : console.log("i dont care i prefer cats");

// exercise 3
// 1. Prompt the user for a number and save it to a variable.
// let input = window.prompt("choose a number");
// input % 2 == 0
//   ? console.log(`${input} is even`)
//   : console.log(`${input} is odd`);

//   exercise 4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

// 1. Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
// If there is no users (the users array is empty), console.log “no one is online”.
// If there is 1 user, console.log “<name_user> is online”.
// If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
// If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
// For example, if there are 5 users, it should display: name_user1, name_user2 and 3 more are online
switch (true) {
  case users.length == 0:
    console.log("no one is online");
    break;
  case users.length == 1:
    console.log(`${users[0]} is online`);
    break;
  case users.length == 2:
    console.log(`${users[0]} and ${users[1]} are online`);
    break;
  default:
    console.log(
      `${users[0]} and ${users[1]} are online as well as ${
        users.length - 2
      } other users`
    );
}
