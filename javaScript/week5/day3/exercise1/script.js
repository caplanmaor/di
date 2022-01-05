function compareToTen(number) {
  let compareNumber = new Promise(function (resolve, reject) {
    if (number > 10) {
      resolve(number + " is greater than 10");
    } else {
      reject(number + " is smaller than 10");
    }
  });
  return compareNumber;
}

compareToTen(15)
  .then((result) => console.log(result))
  .catch((error) => console.log(error));

compareToTen(8)
  .then((result) => console.log(result))
  .catch((error) => console.log(error));
