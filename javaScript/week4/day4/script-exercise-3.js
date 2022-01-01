function getElonMuskDetails({
  first: firstDetail,
  last: lastDetail,
  housesLocation: housesLocationDetail,
  twitter: twitterDetail,
  company: compantDetail,
  houses: { amount: amountDetail, value: valueDetail },
}) {
  console.log(firstDetail, lastDetail, housesLocationDetail, valueDetail);
}

getElonMuskDetails(
  (elonPerson = {
    first: "Elon",
    last: "Musk",
    housesLocation: ["new york", "paris"],
    twitter: "@elonmusk",
    company: "Space X",
    houses: {
      amount: 2,
      value: "5Million",
    },
  })
);
