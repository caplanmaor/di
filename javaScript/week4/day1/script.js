function isPositive(e) {
  return e > 0;
}

let array = [1, 4, 60];
console.log(array.every(isPositive));

function winBattle() {
  return true;
}

function experiencePoints() {
  let points = winBattle() ? 10 : 1;
  return points;
}

console.log(experiencePoints());
