// EXERCISE 1
// Create a function that takes in a single parameter
// and returns a new promise.
// Using setTimeout, after 5000 milliseconds, the promise will either
// resolve or reject.
// If the input is a string, the promise resolves with that same string
// uppercased.
// If the input is anything but a string it rejects with that same input.
// Use `then` to repeat the string twice
// use `catch` to console.log the error
// finally call a function that console.log ("congratulation")

let input = "narnia";
let checkWord = new Promise(function (resolve, reject) {
  setTimeout(() => {
    if (typeof input === "string") {
      resolve(input.toUpperCase());
    } else {
      reject(input);
    }
    console.log(checkWord);
  }, 3000);
});

console.log(checkWord); // should be pending
checkWord.then((result) => console.log(result, result));
checkWord.catch((error) => console.log(error + "!"));
