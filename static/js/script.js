

let modal = document.getElementById("addPostModal");


let btn = document.getElementById("addPostBtn");// Get the button that opens the modal


let closeButton = document.getElementsByClassName("close")[0];// Get the <span> element that closes the modal


btn.onclick = function() {  // When the user clicks on the button, open the modal
  modal.style.display = "block";
};


closeButton.onclick = function() { // When the user clicks on <span> (x), close the modal
  modal.style.display = "none";
};


window.onclick = function(event) {  // When the user clicks anywhere outside of the modal, close it
  if (event.target == modal) {
    modal.style.display = "none";
  }
};