
/* 1047 - Tempo de jogos com minutos - 9 pontos
var [hi, mi, hf, mf] = input.split(' ').map(item => parseInt(item));
mT = 0;

if (hf > hi) {
    hT = (hf - hi);
    if (mf > mi) {
        mT = (mf - mi);
    }
    else if (mf < mi) {
        hT--;
        mT = Math.abs(mf - mi);
        mT = 60 - mT;
    }
} else if (hf < hi) {
    hT = Math.abs(hf - hi);
    hT = 24 - hT;
    if (mf > mi) {
        mT = (mf - mi);
    } else if (mf < mi) {
        hT--;
        mT = Math.abs(mf - mi);
        mT = 60 - mT;
    }
}
else if (hf == hi) {
    if (mf > mi) {
        hT = (hf - hi);
        mT = (mf - mi);
    }
    else if (mf < mi) {
        mT = Math.abs(mf - mi);
        mT = 60 - mT;
        hT = 23;
    }
    else {
        hT = 24;
    }
}

console.log("O JOGO DUROU " + hT + " HORA(S) E " + mT + " MINUTO(S)");
*/

/* 2160 - Nome no Formulário 
    var l;
    l = lines.shift();
    
    if(l.length > 80){
        console.log("NO");
    }
    else{
         console.log("YES");
    }
    */

/*-----------------------------------------------------------------------------------------------------*/

/* 1582 - O teorema de Pitágoras 

var valores = input.split(' ');
lista = [];

for(var i = 0;  i < valores.length-1; i++){
    if(valores[i].length > 1){
        var j = 0;
        var valor = "";
        while(valores[i].length >= j){
            if(/\d/.test(valores[i].charAt(j))){
                    valor += valores[i].charAt(j);
            }
            else{
                 if(valor != ""){
                    lista.push(valor);
                    valor = "";
                 }  
            }
            j++;  
        }    
    }
    else{
        lista.push(valores[i]);
    }
}
 
/*-----------------------------------------------------------------------------------------------------*/

/* 1582 - Toerema de pitágora
var x, y, z;

l = 0, m = 1, n = 2;    
for(var i = 0; i < lines.length; i++){

    x = parseInt(lista[l]);
    y = parseInt(lista[m]);
    z = parseInt(lista[n]);
    
    listaValores = [x, y, z];
    if(pitagora(x, y, z)){
        if(mdcLista(listaValores) == 1){
            console.log("tripla pitagorica primitiva");
        }
        else{
            console.log("tripla pitagorica");
        }
    }
    else{
        console.log("tripla");
    }

    l = l + 3;
    m = m + 3;
    n = n + 3;
} 
function pitagora(a, b, c){
    var res = false;
    if(Math.pow(a, 2) == Math.pow(b, 2) + Math.pow(c, 2) || 
       Math.pow(b, 2) == Math.pow(a, 2) + Math.pow(c, 2) ||
       Math.pow(c, 2) == Math.pow(a, 2) + Math.pow(b, 2)){
       res = true;
    }
    return res;
}
function mdc(a, b){
    if(b == 0) return a;
    return mdc(b, a % b);
}
function mdcLista(numberList){
    var resultado = numberList[0];
    
    for(var i = 0; i < numberList.length; i++){
        resultado = mdc(resultado, numberList[i]);
    }
    return resultado;
}
*/

/*-----------------------------------------------------------------------------------------------------*/

/* 1847 - Bem-vindos e Bem-vindas ao Inverno! 

var [a, b, c] = input.split(' ').map(item => parseInt(item));
 
  if(a > b && b <= c){
    console.log(":)");
}
else if(a < b && b >= c){
    console.log(":(");
}
else if(a < b && b < c){
    if(Math.abs(c-b) < Math.abs(b-a)){
        console.log(":(");
    }
    else{
        console.log(":)");
    }
}

else if(a > b && b > c){
    if(Math.abs(c-b) < Math.abs(b-a)){
        console.log(":)");
    }
    else{
        console.log(":(");
    }
}

else if(a == b){
    if(c > b){
        console.log(":)");
    }
    else{
        console.log(":(");
    }
}*/


/*-----------------------------------------------------------------------------------------------------*/

/* 2344 - Notas da prova 

  var n;
  
  n = parseInt(lines);
  if(n == 0){
      console.log("E");
  }
  else if(n >= 1 && n <= 35){
      console.log("D");
  }
  else if(n >= 36 && n <= 60){
      console.log("C");
  }
  else if(n >= 61 && n <= 85){
      console.log("B");
  }
  else if(n >= 86 && n <= 100){
      console.log("A");
  }
*/

/*-----------------------------------------------------------------------------------------------------*/


/** Triangulo 
 * var [a, b, c, d] = input.split(' ').map(item => parseInt(item));

  forma = false;
  
  var mat = [[a, b, c],[a, b, d],[a, c, d],[b, c, d]];
  for(var i = 0; i < 4; i++){
      if(formatriangulo(mat, i)){
          forma = true;
          break; 
      }
  }
  
  if(forma){
      console.log("S");
  }else{
    console.log("N");
  }
    
   
function formatriangulo(mat, linha){
    if(mat[linha][0] < mat[linha][1] + mat[linha][2] && mat[linha][1] < mat[linha][0] + mat[linha][2] &&
       mat[linha][2] < mat[linha][0] + mat[linha][1]){
        return true;
    }
    return false;
}
*/

/*-----------------------------------------------------------------------------------------------------*/
/*  1161 - Soma de factoriais 
Está correcto, porém, o tamanho do inteiro, não permitiu-lhe armazenar o valor 243290200817664000001  

var valores = input.split(' ');
var lista = [];
for(var i = 0;  i < valores.length; i++){
    if(valores[i].length > 1){
        var j = 0;
        var valor = "";
        while(valores[i].length >= j){
            if(/\d/.test(valores[i].charAt(j))){
                    valor += valores[i].charAt(j);
            }
            else{
                 if(valor !== ""){
                    lista.push(valor);
                    valor = "";
                 }  
            }
            j++;  
        }    
    }
    else{
        lista.push(valores[i]);
    }
}
 
console.log(lista);
l = 0, k = 1;
var m, n, soma = 0;
for(var i = 0; i < lines.length; i++){

    m = parseInt(lista[l]);
    n = parseInt(lista[k]);
    soma = Fatorial(m) + Fatorial(n);
    console.log(soma);
    soma = 0;

    l = l + 2;
    k = k + 2;

}
function Fatorial(x){
    var fatorial = 1;
    for(var i = 1; i <= x; i++){
        fatorial = fatorial * i;
    }
    return fatorial;
}  
*/

/* 2544 - Kage Bushin no Jutsu
while(lines.length > 0){
    n = parseInt(lines[0]);
    
    var i = 0;
    while(parseInt(Math.pow(2, i)) <= n){
        resultado = i;
        i++;
    }
    console.log(resultado);
    lines.shift();
}
*/

/*

var [n1, n2, n3, n4] = input.split(" ").map(item => parseFloat(item));
notaexame = parseFloat(lines[1]);
  
  var media = (n1*2 + n2*3 + n3*4 + n4*1)/(2 + 3 + 4 + 1);
  console.log("Media: " + media.toFixed(1));
  if(media >= 7){
      console.log("Aluno aprovado.");
  }
  else if(media >= 5 && media <= 6.9){
      console.log("Aluno em exame.");
      console.log("Nota do exame: " + notaexame.toFixed(1));
      media = (media + notaexame) / 2;
      
      if(media >= 5){
          console.log("Aluno aprovado.");
      }
      else{
          console.log("Aluno reprovado.");
      }
      console.log("Media final: " + media.toFixed(1));
  }
  else if(media < 5){
      console.log("Aluno reprovado.");
  }


*/
