let userInput1 = "a";
let userInput2 = "b";

async function makeArray() {
  try {
    let promise1 = Promise.resolve(3);
    let promise2 = 42;
    let promise3 = new Promise((resolve, reject) => {
      if ((userInput1 = "a")) {
        resolve("promise3 success");
      } else {
        reject("promise 3 failure");
      }
      setTimeout(resolve, 2000, "foo!");
    });
    let promise4 = new Promise((resolve, reject) => {
      if (userInput2 == "b") {
        resolve("promise 4 success");
      } else {
        reject("promise 4 failure");
      }
    });
    let array = await Promise.all([promise1, promise2, promise3, promise4]);
    console.log(array);
  } catch (error) {
    console.log(error);
  }
}

makeArray();

userInput1 = "x";
userInput2 = "y";

makeArray();
