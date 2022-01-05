let words = ["boat", "africa", "noodles", "puppy"];

function makeArrUpper(arr) {
  let checkPromiseArr = new Promise(function (resolve, reject) {
    if (arr[0] !== null) {
      resolve(makeWordUpper(words));
    } else {
      reject();
    }
  });
  return checkPromiseArr;
}

function sortWords(arr) {
  let checkSortPromiseArr = new Promise(function (resolve, reject) {
    if (arr.every((i) => typeof i === "string")) {
      resolve(arr.sort());
    } else {
      reject();
    }
  });
  return checkSortPromiseArr;
}

makeArrUpper(words)
  .then(sortWords)
  .then((result) => console.log(result))
  .catch((error) => console.log("error", error));

function makeWordUpper(arr) {
  let converted = [];
  for (let e of arr) {
    converted.push(e.toUpperCase());
  }
  return converted;
}
