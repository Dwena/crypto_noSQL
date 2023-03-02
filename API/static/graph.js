const dataCoin = document.getElementById("dataCoin")
console.log(dataCoin)

TESTER = document.getElementById('myPlot');
Plotly.newPlot( TESTER, [{
x: [1, 2, 3, 4, 5],
// x: date,
// y: valeur }], {
y: [1, 2, 4, 8, 16] }], {
margin: { t: 0 } } );