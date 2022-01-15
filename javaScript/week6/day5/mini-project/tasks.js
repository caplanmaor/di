createTasks();
createCheckboxEvent();

function createTasks() {
  //delete old cards
  let holders = document.getElementsByClassName("taskHolder");
  for (let holder of holders) {
    holder.remove();
  }
  //sort tasks
  let tasks = [];
  for (var i = 0; i < localStorage.length; i++) {
    let task = JSON.parse(localStorage.getItem(localStorage.key(i)));
    tasks.push(task);
  }
  tasks.sort((a, b) => new Date(a.startDate) - new Date(b.startDate));
  localStorage.clear();
  for (let task of tasks) {
    localStorage.setItem(task.name, JSON.stringify(task));
  }
  for (let task of tasks) {
    //create task holder
    let taskHolder = document.createElement("div");
    taskHolder.classList.add("taskHolder");
    //create task card
    let taskCard = document.createElement("div");
    taskCard.classList.add("taskCard");
    //create remove button
    let removeButton = document.createElement("button");
    removeButton.innerText = "remove";
    removeButton.addEventListener("click", () => {
      if (confirm("Are you sure?")) {
        localStorage.removeItem(nameText.textContent);
        location.reload();
      }
    });
    taskCard.appendChild(removeButton);
    //create edit button
    let editButton = document.createElement("button");
    editButton.innerText = "edit";
    editButton.addEventListener("click", () => {
      let newName = prompt("choose a new name");
      let srotrageItem = JSON.parse(localStorage.getItem(nameText.textContent));
      let taskName = task.name;
      srotrageItem.name = newName;
      localStorage.setItem(taskName, JSON.stringify(srotrageItem));
      location.reload();
    });
    taskCard.appendChild(editButton);
    //create name text
    let nameText = document.createElement("h1");
    nameText.innerHTML = task.name;
    taskCard.appendChild(nameText);
    //create start date
    let startDate = document.createElement("h2");
    startDate.innerHTML = "start date: " + task.startDate;
    taskCard.appendChild(startDate);
    //create days left
    let endDate = new Date(task.endDate).toLocaleDateString("en-US");
    let nowDate = new Date().toLocaleDateString("en-US");
    let daysLeftText = document.createElement("h2");
    daysLeftText.textContent = "days left to complete: ";
    let diffTime = document.createElement("h2");
    diffTime.innerHTML = Math.ceil(
      (new Date(endDate) - new Date(nowDate)) / (1000 * 60 * 60 * 24)
    );
    taskCard.appendChild(daysLeftText);
    taskCard.appendChild(diffTime);
    // color if passed
    if (diffTime.textContent < 0) {
      taskCard.style.backgroundColor = "red";
    }
    // create checkbox for done
    var checkbox = document.createElement("INPUT");
    checkbox.classList.add("checkbox");
    checkbox.setAttribute("type", "checkbox");
    taskCard.appendChild(checkbox);
    // update from checkbox
    if (task.isDone === true) {
      taskCard.style.backgroundColor = "lightgray";
      checkbox.checked = true;
    }
    // add card to holder
    taskHolder.appendChild(taskCard);
    //create description
    let description = document.createElement("h2");
    description.classList.add("description");
    description.innerHTML = "description: " + task.description;
    taskHolder.appendChild(description);
    //append holder to body
    document.body.appendChild(taskHolder);
  }
}
function createCheckboxEvent() {
  let checkboxes = document.getElementsByClassName("checkbox");
  for (let box of checkboxes) {
    box.addEventListener("change", (e) => {
      if (box.checked) {
        let cardName = box.parentElement.children[2].textContent;
        let srotrageItem = JSON.parse(localStorage.getItem(cardName));
        srotrageItem.isDone = true;
        localStorage.setItem(cardName, JSON.stringify(srotrageItem));
        box.parentElement.style.backgroundColor = "lightgreen";
      } else {
        let cardName = box.parentElement.children[2].textContent;
        let srotrageItem = JSON.parse(localStorage.getItem(cardName));
        srotrageItem.isDone = false;
        localStorage.setItem(cardName, JSON.stringify(srotrageItem));
        box.parentElement.style.backgroundColor = "rgb(224, 236, 240)";
        location.reload();
      }
    });
  }
}
