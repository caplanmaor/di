function divide(numerator, denominator) {
  try {
    if (denominator == 0) {
      throw new Error("cant divide by zero");
    } else {
      return numerator / denominator;
    }
  } catch (err) {
    console.log(err.message);
  }
}

let result = divide(10, 5);
console.log(result);

