
TESTER = document.getElementById('myPlot');
Plotly.newPlot( TESTER, [{
x: [1, 2, 3, 4, 5],
// x: date,
// y: valeur }], {
y: [1, 2, 4, 8, 16] }], {
margin: { t: 0 } } );

const coinClicked = document.getElementsByClassName("coin");

for(let i = 0; i < coinClicked.length; i++) {
    coinClicked[i].addEventListener("click", ouvrirModal)
}
// coinClicked.addEventListener("click", ouvrirModal);

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