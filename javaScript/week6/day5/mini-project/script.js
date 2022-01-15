let input = {
  name: "",
  description: "",
  startDate: "",
  endDate: "",
  isDone: false,
};

const nameInput = document.querySelector("input");
const form = document.querySelector("form");

nameInput.addEventListener("input", () => {
  nameInput.setCustomValidity("");
  nameInput.checkValidity();
});

nameInput.addEventListener("invalid", () => {
  if (nameInput.value === "") {
    nameInput.setCustomValidity("Enter your username!");
  } else {
    nameInput.setCustomValidity(
      "Usernames can only contain upper and lowercase letters. Try again!"
    );
  }
});

document.getElementById("submit-btn").addEventListener("click", (event) => {
  saveItems();
});

function saveItems() {
  input.name = document.getElementById("name").value;
  input.description = document.getElementById("description").value;
  input.startDate = document.getElementById("startDate").value;
  input.endDate = document.getElementById("endDate").value;
  localStorage.setItem(input.name, JSON.stringify(input));
}
