document.addEventListener("DOMContentLoaded", function () {
  const audioPlayer = document.getElementById("listen");
  const playIcon = document.querySelector(".material-symbols-outlined");

  playIcon.addEventListener("click", function () {
    audioPlayer.play();
  });
});

var today = new Date();

// Format the date as needed
var formattedDate = today.getFullYear();

// Display the date using jQuery
$("#dateDisplay").text("Today's Date: " + formattedDate);
