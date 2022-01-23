//Exercise 1 : Change The Navbar

// 1 In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

document.getElementById("navBar").setAttribute("id", "socialNetworkNavigation");

// 2. Add a new <li> to the <ul>
// First, create a new <li> tag (use the createElement method)
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.

let ul = document.getElementsByTagName("ul")[0];
let logOutLi = document.createElement("li");
let logOutNode = document.createTextNode("LogOut");
logOutLi.appendChild(logOutNode);
ul.appendChild(logOutLi);

// 3.Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements from their parent element (ul). Display the text of each link. (Hint: use the textContent property).
let firstLink = ul.firstElementChild;
console.log(firstLink.textContent);

let lastLink = ul.lastElementChild;
console.log(lastLink.textContent);
