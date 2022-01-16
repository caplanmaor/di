//print a pyramid of *
let size = 5;

//one loop
let output = "";
for (let i = 0; i < size; i++) {
  output += " * ";
  console.log(output);
}

//two loops
for (let i = 0; i < size; i++) {
  let output2 = "";
  for (let j = 0; j < i + 1; j++) {
    output2 += " * ";
  }
  console.log(output2);
}
