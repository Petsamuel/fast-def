document.addEventListener("DOMContentLoaded", function () {
  const audioPlayer = document.getElementById("listen");
  const playIcon = document.querySelector(".material-symbols-outlined");

  playIcon.addEventListener("click", function () {
    audioPlayer.play();
  });
});

var today = new Date();

// Format the date as needed
var formattedDate =
  today.getFullYear() +
  "-" +
  (today.getMonth() + 1).toString().padStart(2, "0") +
  "-" +
  today.getDate().toString().padStart(2, "0");

// Display the date using jQuery
jQuery(document).ready(function ($) {
  $("#dateDisplay").text("Today's Date: " + formattedDate);
  console.log(formattedDate);

});