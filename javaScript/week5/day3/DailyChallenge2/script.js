let morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`;
//   let morseArrValues = Object.values(morseObj);
//   let morseArrKeys = Object.keys(morseObj);

let input = "Hello";
let morseObj = {};
let translatedWord = [];

// convert string to Object
function toObj(morseString) {
  let convertToObj = new Promise(function (resolve, reject) {
    morseObj = JSON.parse(morseString);
    if (morseObj == null) {
      reject("error morse object is empty");
    } else {
      resolve(morseObj);
    }
  });
  return convertToObj;
}

//convert word to morse code
function toMorse(obj) {
  let convertToMorse = new Promise(function (resolve, reject) {
    let isInObj = null;
    //check if the characters are in the obj
    let morseArrKeys = Object.keys(obj);
    for (let letter of input.toLowerCase()) {
      if (morseArrKeys.includes(letter)) {
        isInObj = true;
      } else {
        reject("letters not in dictionary");
      }
    }
    //translate
    let morseArrValues = Object.values(obj);
    if (isInObj === true) {
      for (let letter of input.toLowerCase()) {
        morseArrKeys.forEach((e, i) => {
          if (letter == e) {
            translatedWord.push(morseArrValues[i]);
          }
        });
      }
    }
  });
  return convertToMorse;
}

//convert translated array to string
function toString(arr) {
  let stringResult = arr.join("\r\n");
  console.log(stringResult);
}

console.log(translatedWord);

toObj(morse)
  .then(toMorse(morseObj))
  .then(toString(translatedWord))
  .then((result) => console.log(result))
  .catch((error) => console.log(error));
