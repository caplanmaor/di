let isAnagram = true;

let anagram = [..."cat"];
let testWord = [..."act"];

function checkAnagram() {
  anagram.forEach((e) => {
    testWord.includes(e) ? null : (isAnagram = false);
  });
  console.log(isAnagram);
}

checkAnagram();

//testing false
anagram = [..."catzzz"];
checkAnagram();
