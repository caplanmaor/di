let sentence = "that book is not that bad, i like it";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (wordBad > wordNot) {
  console.log(
    `${sentence.slice(0, wordNot)}good${sentence.slice(wordBad + 3)}`
  );
} else {
  console.log(sentence);
}
