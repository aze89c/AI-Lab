/*
%JOHN THE THIEF STATEMENTS 
 
THERE'S A THIEF WINI WHO LIKES A BALL. 
THERE'S A THIEF WILLIAM WHO LIKES A SHOE. 
THERE'S A THIEF JOHN WHO LIKES SNOW AND DOLLAR. 
FIND THE STEALING PERSON AND LIKES. 
*/

 
%PROGRAM 
 
thief(wini). 
thief(john). 
thief(willisam). 
likes(wini,ball). 
likes(william,shoe). 
likes(john,snow). 
 
likes(john,dollar). 

may_steal(john,X) :-thief(john), likes(john,X). 

/*

OUTPUT


GNU Prolog 1.5.0 (64 bits)
Compiled Jul  8 2021, 12:22:53 with gcc
Copyright (C) 1999-2021 Daniel Diaz

| ?- change_directory('C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)').

yes
| ?- [basics4].
compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics4.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics4.pl compiled, 27 lines read - 1156 bytes written, 4 ms

yes
| ?- likes(john,X).

X = snow ? ;

X = dollar

yes
| ?- likes(john,Z).

Z = snow ? ;

Z = dollar

yes
| ?- likes(john,D).

D = snow ? ;

D = dollar

yes
| ?- may_steal(john,X). 

X = snow ? 

yes

| ?- likes(john,D).

D = snow ? ;

D = dollar

yes
| ?- may_steal(john,ball). 

no
| ?- may_steal(john,dollar). 

yes

*/