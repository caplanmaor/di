function printSuccess() {
  let printWord = new Promise(function (resolve, reject) {
    setTimeout(function () {
      resolve("success");
      reject("oops something went wrong");
    }, 4000);
  });
  return printWord;
}

printSuccess()
  .then((result) => console.log(result))
  .then((error) => console.log(error));
