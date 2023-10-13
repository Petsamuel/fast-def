document.addEventListener("DOMContentLoaded", function () {
  const audioPlayer = document.getElementById("listen");
  const playIcon = document.querySelector(".material-symbols-outlined");

  playIcon.addEventListener("click", function () {
    audioPlayer.play();
  });
});

alert("testing..");
