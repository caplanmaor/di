let guesses = 3;

function playTheGame() {
  if (confirm("wanna play?")) {
    let userNumber = prompt("choose a number 0 - 10");
    while (isNaN(userNumber) || userNumber > 11 || userNumber < -1) {
      userNumber = prompt("no letters, only 1-10");
    }
    let pcNumber = Math.floor(Math.random() * 11);
    console.log(pcNumber);
    while (userNumber !== pcNumber) {
      while (guesses > 0) {
        guesses = guesses - 1;
        test(userNumber, pcNumber);
        userNumber = prompt(`guess again, ${guesses} tries`);
      }
      console.log("the game is over");
      return;
    }
    // window.alert("you won, you guessed the correct number");
  } else {
    window.alert("fine bye");
  }
}

function test(user, pc) {
  if (user == pc) {
    window.alert("you won, you guessed the correct number");
    window.alert("the game is over");
    return;
  } else if (user > pc) {
    window.alert("your number is bigger");
  } else if (user < pc) {
    window.alert("your number is smaller");
  }
}
