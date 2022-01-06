// let selectFrom = document.getElementById("selectfrom");
let selectTo = document.getElementById("selectto");
let supportedCurrencies = {};

//get supported currencies
async function getCurrencies() {
  try {
    let avilableCurrencies = await fetch(
      "http://api.currencylayer.com/list?access_key=6b543e9294a71d26a6606f5449cf71a6&format=1"
    );
    supportedCurrencies = await avilableCurrencies.json();
    supportedCurrencies = supportedCurrencies.currencies;
    let supportedCurrenciesArr = Object.values(supportedCurrencies);
    populateSelects(supportedCurrenciesArr);
  } catch (error) {
    console.log(error);
  }
}

async function getRates() {
  try {
    //get value from form
    // var fromValue = selectFrom.options[selectFrom.selectedIndex].value;
    var toValue = selectTo.options[selectTo.selectedIndex].value;
    // convert form value to id
    // let fromKey = convertNameToId(fromValue);
    let toKey = convertNameToId(toValue);
    // get conversion rates
    let conversionRatesFetch = await fetch(
      `http://api.currencylayer.com/live?access_key=6b543e9294a71d26a6606f5449cf71a6&source=USD&currencies=${toKey}`
    );
    let conversionRatesObj = await conversionRatesFetch.json();
    let quotes = conversionRatesObj.quotes;
    let rate = Object.values(quotes)[0];
    // get the value the user wanted
    let value = document.getElementById("amount").value;
    // print result
    document.getElementById("result").innerHTML = value * rate;
  } catch (error) {
    console.log(error);
  }
}

getCurrencies();

document.getElementById("convert").addEventListener("click", (e) => {
  e.preventDefault();
  getRates();
});

function populateSelects(curArr) {
  //put items in from
  //   for (let cur of curArr) {
  //     let opt = document.createElement("option");
  //     opt.value = cur;
  //     opt.innerHTML = cur;
  //     selectFrom.appendChild(opt);
  //   }
  //put items in to
  for (let cur of curArr) {
    let opt = document.createElement("option");
    opt.value = cur;
    opt.innerHTML = cur;
    selectTo.appendChild(opt);
  }
}

function convertNameToId(name) {
  let optionId = "";
  let supCurValues = Object.values(supportedCurrencies);
  supCurValues.forEach((element, i) => {
    if (element == name) {
      let supCurKeys = Object.keys(supportedCurrencies);
      optionId = supCurKeys[i];
      console.log(optionId);
    }
  });
  return optionId;
}
