/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

grammar gcode;

options {
    language = Python3;
}


def 	:	statement+ fimprograma
	;
	
fimprograma 
	:	numerolinha mfim
	;
		
statement 
	:	numerolinha codfunc coordx coordy fimdelinha
	|   numerolinha codfunc coordx coordy coordi coordj fimdelinha
    |   numerolinha codfunc coordx fimdelinha
    |   numerolinha codfunc coordy fimdelinha
	|	numerolinha mfunc fimdelinha
	|   fimdelinha
	;

numerolinha 
	:	'N' NUMBER
	;

num3dig : NUMBER NUMBER NUMBER ;

mfim 	:	'M30'
	;
	
mfunc 
	:	'M02'
	|	'M01' STRING
	;
	
codfunc :	'G01'
	|	'G00'
	|   'G02'
	;
	
coordx 	:	'X'coord
	;

coordy 	:	 'Y'coord
	;
		
coordi
    : 'I' coord
    ;

coordj
    : 'J' coord
    ;

coord   :       NUMBER
        ;

fimdelinha :	'\r\n'
	|	'\n'
	;
			
NUMBER : '-'? [0-9]+ ;
	
WS : [ \t\r\n]+ -> skip ;
	
STRING  :  '"' ( ESC_SEQ | ~('\\'|'"') )* '"'
    ;

fragment
HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ;

fragment
ESC_SEQ
    :   '\\' ('b'|'t'|'n'|'f'|'r'|'\\')
    |   UNICODE_ESC
    |   OCTAL_ESC
    ;

fragment
OCTAL_ESC
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;

fragment
UNICODE_ESC
    :   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
    ;


