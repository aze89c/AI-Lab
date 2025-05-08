/*
%fact and query knowledge base STATEMENTS 
 
A DOG NAME IS SAM 
A DOG NAME IS HENRY 
A CAT NAME IS FELIX 
A CAT NAME IS MICHAEL 
FIND DOG AND CAT IN THIS QUERY 
*/

 
%PROGRAM 
 
dog(sam). 
dog(henry). 
cat(felix). 
cat(jame). 
cat(michael). 
animal(X):-dog(X). 
animal(Y):-cat(Y).

/*
OUTPUT

GNU Prolog 1.5.0 (64 bits)
Compiled Jul  8 2021, 12:22:53 with gcc
Copyright (C) 1999-2021 Daniel Diaz

| ?- change_directory('C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)').

yes
| ?- [basics5].
compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics5.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics5.pl compiled, 19 lines read - 754 bytes written, 5 ms

yes
| ?- animal(X).

X = sam ? ;

X = henry ? ;

X = felix ? ;

X = jame ? ;

X = michael

yes
| ?- animal(Y).

Y = sam ? ;

Y = henry ? ;

Y = felix ? ;

Y = jame ? 

yes
| ?- dog(X).

X = sam ? ;

X = henry

yes
| ?- cat(X).

X = felix ? ;

X = jame ? ;

X = michael

yes
| ?- cat(Y).

Y = felix ? '
Action (; for next solution, a for all solutions, RET to stop) ? ;

Y = jame ? ;

Y = michael

yes


*/