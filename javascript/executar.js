// var input = require('fs').readFileSync('stdin', 'utf8');
// var lines = input.split('\n');

// var avancar = document.getElementById('avancar')
// var regressar = document.getElementById('regressar')

var x = 0;

var btn1 = document.createElement('button');
var btn2 = document.createElement('button');
var resultado = document.createElement('p');

var div = document.cre


var texto1 = document.createTextNode('Regressar');
var texto2 = document.createTextNode('Avançar');
var texto3 = document.createTextNode('0');


btn1.appendChild(texto1);
btn2.appendChild(texto2);
resultado.appendChild(texto3);

btn2.addEventListener('click', () => {
    x++;
    texto3.nodeValue = x;
})

btn1.addEventListener('click', () => {
    x--;
    texto3.nodeValue = x;
})




document.body.appendChild(btn1);
document.body.appendChild(resultado);
document.body.appendChild(btn2);







/* ------------------------------------------------------------------------------ */



/* ------------------------------------------------------------------------------ */