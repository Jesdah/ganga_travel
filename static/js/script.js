

let postModal = document.getElementById("addPostModal");


let postBtn = document.getElementById("addPostBtn");// Get the button that opens the modal


let closeButton = document.getElementsByClassName("close")[0];// Get the <span> element that closes the modal


postBtn.onclick = function() {  // When the user clicks on the button, open the modal
  postModal.style.display = "block";
};


closeButton.onclick = function() { // When the user clicks on <span> (x), close the modal
  postModal.style.display = "none";
};


window.onclick = function(event) {  // When the user clicks anywhere outside of the modal, close it
  if (event.target == postModal) {
    postModal.style.display = "none";
  }
};


