function print3() {
  let printWord = new Promise(function (resolve, reject) {
    setTimeout(function () {
      resolve("success");
      reject("oops something went wrong");
    }, 1000);
  });
  return printWord;
}

function printBoo() {
  let printWord = new Promise(function (resolve, reject) {
    setTimeout(function () {
      let x = 1;
      if (x == 2) {
        resolve("success");
      } else {
        reject("Boo!");
      }
    }, 1000);
  });
  return printWord;
}

print3()
  .then((result) => console.log(result))
  .catch((error) => console.log(error));
printBoo()
  .then((result) => console.log(result))
  .catch((error) => console.log(error));
