<?php

    /* 1047 - Tempo de jogos com minutos - 9 pontos */
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
    
    print("O JOGO DUROU " + $hT + " HORA(S) E " + $mT + " MINUTO(S)"."\n");
    
?>