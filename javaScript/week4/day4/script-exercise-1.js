// Pass this object
// Details = { name: "Harry Potter", house: "Gryfindor", goodstudent: false };
// as an argument of the getDetails function.
// Destructure the object in the parameter (ie. you should have 3 parameters : name, house and goodstudents)

function getDetails({
  detailName: name,
  detailHouse: house,
  detailGoodStudent: goodstudent,
}) {
  console.log(name, house, goodstudent);
}

getDetails({
  detailName: "Harry Potter",
  detailHouse: "Gryfindor",
  detailGoodStudent: false,
});
