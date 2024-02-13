<?php

   /* 1047 - Tempo de jogos com minutos - 9 pontos 
       $hT = 0;
       $mT = 0;

       $valores = explode(" ", fgets(STDIN));
       $hi = (int)$valores[0];
       $mi = (int)$valores[1];
       $hf = (int)$valores[2];
       $mf = (int)$valores[3];

 
     
    if($hf > $hi){
        $hT = ($hf-$hi);
        if($mf > $mi){
            $mT = ($mf-$mi);
        }
        else if($mf < $mi){
            $hT--;
            $mT = abs($mf-$mi);
            $mT = 60 - $mT;
        }
    }else if($hf < $hi){
        $hT = abs($hf-$hi);
        $hT = 24-$hT;
        if($mf > $mi){
            $mT = ($mf-$mi); 
       }else if($mf < $mi){
            $hT--;
            $mT = abs($mf-$mi);
            $mT = 60 - $mT;
        }
    }
    else if($hf == $hi){
        if($mf > $mi){
            $hT=($hf-$hi);
            $mT = ($mf-$mi); 
       }
        else if($mf < $mi){
            $mT = abs($mf-$mi);
            $mT = 60 - $mT;
            $hT=23;
        }
        else{
            $hT = 24;
        }
    }
    
    print("O JOGO DUROU " . $hT ." HORA(S) E " . $mT . " MINUTO(S)"."\n");

    */

/*
$p = 0;
$valores = explode(" ", fgets(STDIN));
$n = (int)$valores[0];
$l = (int)$valores[1];

$p = $n*$l;
echo $p. "\n";

*/


/* 1837 - Prefácio
$valores = explode(" ", fgets(STDIN));
    $a = (int)$valores[0];
    $b = (int)$valores[1];
    if($a < 0 && $b > 0){
        $i =-1;
        while($i*$b > $a){
            $i--;
        }
        $q = $i;
        $r = $a - ($i*$b);
    }
    else if( $a < 0 && $b < 0){
        $i = 1;
        while($i*$b > $a){
            $i++;
        }
        $q = $i;
        $r = $a - ($i*$b);
    }
    else{
        $q = (int)($a / $b);
        $r = $a % $b;
    }
    print("$q $r"."\n");
    */

?>