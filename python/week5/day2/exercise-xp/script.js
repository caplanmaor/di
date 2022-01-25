// Exercise 1
// Using a DOM property, retrieve the h1 and console.log it.
let h1 = document.getElementsByTagName("h1")[0].innerText;
console.log(h1);

// Using DOM methods, remove the last paragraph in the <article> tag.
let allParagraphs = document.getElementsByTagName("p");
allParagraphs[3].remove();

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on
let theChoclate = document.getElementsByTagName("h2");
theChoclate[0].addEventListener("click", () => {
  theChoclate[0].style.backgroundColor = "red";
});

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
let history = document.getElementsByTagName("h3");
history[0].addEventListener("click", () => {
  history[0].style.display = "none";
});

// Add a <button> to the HTML file, that when clicked on,
// should make the text of all the paragraphs, bold.

let text = document.createTextNode("bold all");
let button = document.createElement("button");
button.appendChild(text);
button.addEventListener("click", () => {
  article[0].style.fontWeight = "bold";
});
let article = document.getElementsByTagName("article");
article[0].appendChild(button);

// Exercise 2
// Retrieve the form and console.log it.
let form = document.getElementsByTagName("form");
console.log(form[0]);

// Retrieve the inputs by their id and console.log them.
let inputs = [];
inputs.push(document.getElementById("fname"), document.getElementById("lname"));
console.log(inputs);

// Retrieve the inputs by their name attribute and console.log them.
console.log(
  document.getElementsByName("fname")[0],
  document.getElementsByName("lname")[0]
);

// When the user submits the form (ie. submit event listener)
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.

document.getElementById("submit").addEventListener("click", (e) => {
  e.preventDefault();
  let fname = document.getElementById("fname").value;
  let lname = document.getElementById("lname").value;
  if (fname !== "" && lname !== "") {
    let ul = document.getElementsByClassName("usersAnswer")[0];
    let fnameLi = document.createElement("li");
    fnameLi.innerHTML = fname;
    let lnameLi = document.createElement("li");
    lnameLi.innerHTML = lname;
    ul.appendChild(fnameLi);
    ul.appendChild(lnameLi);
  }
});

// Exercise 3
//Create a global variable named allBoldItems.
// Create a function called getBold_items() that takes no parameter.
// This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

const getBold_Items = () => {
  let allBoldItemsCollection = document.getElementsByTagName("strong");
  let allBoldItems = [];
  for (let i = 0; i < allBoldItemsCollection.length; i++) {
    allBoldItems.push(allBoldItemsCollection[i].innerHTML);
  }
  console.log(allBoldItems);
};
getBold_Items();

// Create a function called highlight() that changes the color of all the bold text to blue.
let allBoldItemsCollection = document.getElementsByTagName("strong");
let allBoldItems = [];
for (let i = 0; i < allBoldItemsCollection.length; i++) {
  allBoldItems.push(allBoldItemsCollection[i].innerHTML);
}

function highlight() {
  let sentance = document.getElementsByTagName("p")[3].innerText;
  allBoldItems.forEach((element) => {
    sentance = sentance.replace(
      element,
      `<span style='color:blue'>${element}</span>`
    );
  });
  document.getElementsByTagName("p")[3].innerHTML = sentance;
}

// Create a function called return_normal() that changes the color of all the bold text back to black.
function return_normal() {
  let sentance = document.getElementsByTagName("p")[3].innerText;
  allBoldItems.forEach((element) => {
    sentance = sentance.replace(element, `<strong>${element}</strong>`);
  });
  document.getElementsByTagName("p")[3].innerHTML = sentance;
}

//Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

document.getElementsByTagName("p")[3].addEventListener("mouseover", () => {
  highlight();
});

document.getElementsByTagName("p")[3].addEventListener("mouseout", () => {
  return_normal();
});

// Exercise 4
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:

document.getElementById("sphereSubmit").addEventListener("click", (e) => {
  e.preventDefault();
  let radius = document.getElementById("radius").value;
  document.getElementById("volume").value =
    (4 * Math.PI * radius * radius * radius) / 3;
});
