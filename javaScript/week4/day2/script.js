//landscape
let landscape = () => {
  let result = "";

  let flat = (x) => {
    for (let count = 0; count < x; count++) {
      result = result + "_";
    }
  };

  let mountain = (x) => {
    result = result + "/";
    for (let counter = 0; counter < x; counter++) {
      result = result + "'";
    }
    result = result + "\\";
  };

  flat(4);
  mountain(4);
  flat(4);
  mountain(2);
  flat(8);

  return result;
};
console.log(landscape());

//daily challenge
function setList(list) {
  //list.totalPrice = "35$"
  //list.other.payed = false;
  list = {
    fruits: ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice: "35$",
    other: {
      payed: false,
      meansOfPayment: ["cash", "creditCard"],
    },
  };
  return list;
}

let groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    payed: true,
    meansOfPayment: ["cash", "creditCard"],
  },
};

let copy = setList(groceries);

console.log(groceries);
console.log(copy);

//the price 34 should appear on both
