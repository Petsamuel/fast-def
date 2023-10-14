document.addEventListener("DOMContentLoaded", function () {
  const audioPlayer = document.getElementById("listen");
  const playIcon = document.querySelector(".material-symbols-outlined");

  playIcon.addEventListener("click", function () {
    audioPlayer.play();
  });
});

$(document).click(function () {
  $("#toggle").effect("shake");
});

$("#notification").fadeIn();

    // Automatically close the notification after 5 seconds (5000 milliseconds)
    setTimeout(function () {
      $("#notification").fadeOut();
    }, 5000);