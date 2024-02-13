

/* 1047 - Tempo de jogos com minutos - 9 pontos 

  String input = stdin.readLineSync().toString();
  final List<String> valores = input.split(' ');

  int hT = 0, mT = 0;

  int hi = int.parse(valores[0]);
  int mi = int.parse(valores[1]);
  int hf = int.parse(valores[2]);
  int mf = int.parse(valores[3]);

  if (hf > hi) {
    hT = (hf - hi);
    if (mf > mi) {
      mT = (mf - mi);
    } else if (mf < mi) {
      hT--;
      if (mf > mi) {
        mT = (mf - mi);
      } else {
        mT = (mi - mf);
      }

      mT = 60 - mT;
    }
  } else if (hf < hi) {
    if (hf > hi) {
      hT = hf - hi;
    } else {
      hT = hi - hf;
    }
    hT = 24 - hT;
    if (mf > mi) {
      mT = (mf - mi);
    } else if (mf < mi) {
      hT--;
      if (mf > mi) {
        mT = (mf - mi);
      } else {
        mT = (mi - mf);
      }
      mT = 60 - mT;
    }
  } else if (hf == hi) {
    if (mf > mi) {
      hT = (hf - hi);
      mT = (mf - mi);
    } else if (mf < mi) {
      if (mf > mi) {
        mT = (mf - mi);
      } else {
        mT = (mi - mf);
      }
      mT = 60 - mT;
      hT = 23;
    } else {
      hT = 24;
    }
  }

  print("O JOGO DUROU " +
      hT.toString() +
      " HORA(S) E " +
      mT.toString() +
      " MINUTO(S)");
      */


/* 1296 - Mediana 
double m1, m2, m3, l1, l2, l3, p, a;

  while (true) {
    var e = stdin.readLineSync();
    if (e == null) break;

    final List<String> valores = e.split(" ");
    m1 = double.parse(valores[0]);
    m2 = double.parse(valores[1]);
    m3 = double.parse(valores[2]);

    l3 = sqrt((8 * pow(m1, 2) + 8 * pow(m2, 2) - 4 * pow(m3, 2)) / 9);
    l2 = sqrt((8 * pow(m1, 2) + 4 * pow(m2, 2) - 6 * pow(l3, 2)) / 3);
    l1 = sqrt(2 * (pow(l2, 2) + pow(l3, 2)) - 4 * pow(m1, 2));

    if (l1 < l2 + l3 && l2 < l1 + l3 && l3 < l1 + l2) {
      p = (l1 + l2 + l3) / 2;
      a = sqrt(p * (p - l1) * (p - l2) * (p - l3));
      print(a.toStringAsFixed(3));
    } else {
      print("-" + 1.toStringAsFixed(3));
    }
  } 
  */


/*Ler valores na mesma linha
import 'dart:io'; 
void main(List<String> args) {
  
String input = stdin.readLineSync().toString();
final List<String> valores = input.split(' ');

  int a = int.parse(valores[0]);
  int b = int.parse(valores[1]);
  int c = int.parse(valores[2]);

  int maior = (a + b + (a > b ? a - b : b - a)) ~/ 2;
  if (maior < c) {
    maior = c;
  }
  print('$maior eh o maior');
  }
  */



/* 1219 - Flores cloridas

  int a, b, c;
   const double PI = 3.1415926535897;

  while (true) {
    var e = stdin.readLineSync();
    if (e == null) break;

    final List<String> valores = e.split(' ');

    int a = int.parse(valores[0]);
    int b = int.parse(valores[1]);
    int c = int.parse(valores[2]);

    double R, r, Area_triangulo, Area_amarela, Area_azul, Area_vermelha, p;
    p = (a + b + c) / 2;

    Area_triangulo = sqrt(p * (p - a) * (p - b) * (p - c));
    R = (a * b * c) / (4.0 * Area_triangulo);

    Area_amarela = PI * pow(R, 2) - Area_triangulo;

    r = Area_triangulo / p;
    Area_azul = Area_triangulo - PI * pow(r, 2);

    Area_vermelha = PI * pow(r, 2);

    print(Area_amarela.toStringAsFixed(4) + " " + Area_azul.toStringAsFixed(4) + " " + Area_vermelha.toStringAsFixed(4));
}
*/



   /* 2544 - Kage Bushin no Jutsu - Termina com fim de arquivo EOF
  int n, i, resultado = 0;
  while (true) {
    var e = stdin.readLineSync();
    if (e == null) break;
    n = int.parse(e.toString());
    i = 0;
    while (pow(2, i) <= n) {
      resultado = i;
      i++;
    }
    print(resultado.toString());
  }
  */