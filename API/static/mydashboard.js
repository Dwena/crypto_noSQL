function ouvrirModal(name, image, date, valeur) {
    console.log(image)
    document.getElementById("modal-nom").innerHTML = name;
    // document.getElementById("modal-nom").innerHTML = date;
    // document.getElementById("modal-nom").innerHTML = valeur;
    imageLogo = document.getElementById("modal-image")
    imageLogo.src = image;
    document.getElementById("modal").style.display = "block";
    TESTER = document.getElementById('myPlot');
    Plotly.newPlot( TESTER, [{
    x: [1, 2, 3, 4, 5],
    y: [1, 2, 4, 8, 16] }], {
    margin: { t: 0 } } );
}

function fermerModal() {
    document.getElementById("modal").style.display = "none";
}