let input = window.prompt("write several words");
let inputArray = input.split(" ");
let longestWord = inputArray.reduce(function (a, b) {
  return a.length > b.length ? a : b;
});
let output = "";
for (let i = 0; i <= longestWord.length / 2; i++) {
  output += "* ";
}
console.log(`* ${output}*`);
inputArray.forEach((element) => {
  let spaceSize = longestWord.length - element.length;
  let space = "";
  for (let i = 0; i < spaceSize; i++) {
    space += " ";
  }

  console.log(`* ${element}${space} *`);
});
console.log(`* ${output}*`);
