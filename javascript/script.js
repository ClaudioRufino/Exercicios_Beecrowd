var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');
    
// var [a, b, c] = input.split(' ').map(item => parseInt(item));


// while(scan.hasNext()){
//     long m = 1;
//     int digitos = 1;
//     int n = scan.nextInt();
//     while((m % n != 0)){
//         m = (10*m+1)%n;
//         digitos++;
//     }
//     System.out.println(digitos);
// }
// scan.close();

while(lines.length > 0){
    var m = 1;
    var digitos = 1;
    var n = parseInt(lines[0]);
    while((m % n != 0)){
        m = (10*m+1)%n;
        digitos++;
    }
    console.log(digitos);
    
    lines.shift();
}
        
        
        
        
    
    
 
    




