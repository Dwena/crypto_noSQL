const coinClicked = document.getElementsByClassName("coin");

// coinClicked.addEventListener("click", ouvrirModal);
for(let i = 0; i < coinClicked.length; i++) {
    coinClicked[i].addEventListener("click", ouvrirModal)
}

function ouvrirModal() {
    console.log("date, valeur")
    // document.getElementById("modal-nom").innerHTML = name;
    // imageLogo = document.getElementById("modal-image")
    // imageLogo.src = image;
    // document.getElementById("modal").style.display = "block";
}

function fermerModal() {
    document.getElementById("modal").style.display = "none";
}