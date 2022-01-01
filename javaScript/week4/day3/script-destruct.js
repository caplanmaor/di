// //SPREAD OPERATOR
// let letters = ["a", "b", "c"];
// let numbers = [1, 2, 3];
// let newArr = [...letters, ...numbers];
// console.log(newArr);

// //spreading
// //dots before an array
// function test(a, b) {
//   console.log("a : ", a, "b ", b);
// }

// test(...["blue", "red"]);

//resting
//dots before an variable name
// function testOne(...colors) {
//   console.log("colors : ", colors);
// }

// testOne("blue", "red");

//Copying
//Copying by reference
// let names = ["John", "Tom"];
// let friends = names; //they both have the same reference
// friends.push("Lea");
// console.log("friends : ", friends, "names ", names);

//Coppying by Value with the spread operator
// let newFriends = [...names];
// console.log("newFriends : ", newFriends);
// newFriends.push("Lea");
// console.log("newFriends : ", newFriends, "names ", names);

// Copying
// Shallow copy
let newNames = ["John", "Tom", ["blue", "red"]];
let newNamesClone = [...newNames];
newNamesClone[2].push("yellow");
console.log(newNames, newNamesClone);
