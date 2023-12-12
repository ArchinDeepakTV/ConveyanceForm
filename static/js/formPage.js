function getDay(selectedDate) {
  var selectedDay = new Date(selectedDate).getDay();
  document.getElementById("day").value = days[selectedDay];
}

function updateDistance() {
  document.getElementById("distance").value = "Auto";
}

function handleFormSubmission() {
  // your code to submit the form goes here
  return false; // this prevents the form from being submitted
}

var days = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
];
