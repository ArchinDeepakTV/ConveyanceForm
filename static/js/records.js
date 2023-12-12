const d = new Date();
let currentYear = d.getFullYear();
let currentMonth = d.getMonth();

const year = document.getElementById("year");
console.log(year);

const yearList = {};
for (let i = 2023; i <= currentYear; i++) {
  //   yearList.Add(i, i.toString());
  yearList[i] = i.toString();
  console.log(yearList);
}
for (let key in yearList) {
  let option = document.createElement("option");
  option.setAttribute("value", yearList[key]);
  let optionText = document.createTextNode(key);
  option.appendChild(optionText);

  year.appendChild(option);
}

const month = document.getElementById("month");
console.log(month);

const monthList = {};
for (let i = 0; i <= currentMonth; i++) {
  if (i == 0) monthList["January"] = "jan";
  if (i == 1) monthList["February"] = "feb";
  if (i == 2) monthList["March"] = "mar";
  if (i == 3) monthList["April"] = "apr";
  if (i == 4) monthList["May"] = "may";
  if (i == 5) monthList["June"] = "jun";
  if (i == 6) monthList["July"] = "jul";
  if (i == 7) monthList["August"] = "aug";
  if (i == 8) monthList["September"] = "sep";
  if (i == 9) monthList["October"] = "oct";
  if (i == 10) monthList["November"] = "nov";
  if (i == 11) monthList["December"] = "dec";
  console.log(monthList);
}
for (let key in monthList) {
  let option = document.createElement("option");
  option.setAttribute("value", monthList[key]);
  let optionText = document.createTextNode(key);
  option.appendChild(optionText);

  month.appendChild(option);
}