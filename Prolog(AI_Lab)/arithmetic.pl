%PROGRAM OF ARITHMETIC OPERATION 
 
sum(X,Y):- S is X+Y, 
write(S), /*You can just the "write" function without the use of "nl", "nl" is just used for printing in a new line incase if we decide to print sum, sub,  mul and div together. */
nl. 


sub(X,Y):- S is X-Y, 
write(S),/*You can just the "write" function without the use of "nl", "nl" is just used for printing in a new line incase if we decide to print sum, sub,  mul and div together. */
nl.

 
mul(X,Y):- M is X*Y, 
write(M),/*You can just the "write" function without the use of "nl", "nl" is just used for printing in a new line incase if we decide to print sum, sub,  mul and div together. */
nl.
 

div(X,Y):- D is X/Y, 
write(D),/*You can just the "write" function without the use of "nl", "nl" is just used for printing in a new line incase if we decide to print sum, sub,  mul and div together. */
nl.


/*
Without the use of "nl"(new line).
OUTPUT

GNU Prolog 1.5.0 (64 bits)
Compiled Jul  8 2021, 12:22:53 with gcc
Copyright (C) 1999-2021 Daniel Diaz

| ?- change_directory('C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)').

yes

| ?- 
[arithmetic].
compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/arithmetic.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/arithmetic.pl compiled, 18 lines read - 1586 bytes written, 9 ms

yes
| ?- sum(10,36).
46

yes
| ?- mul(99,2).
198

yes
| ?- mul(99,2), sum(10,1).
19811

yes
| ?- div(10,4).
2.5

yes

*/

/*

OUTPUT

With the use of "nl"(new line).

GNU Prolog 1.5.0 (64 bits)
Compiled Jul  8 2021, 12:22:53 with gcc
Copyright (C) 1999-2021 Daniel Diaz

| ?- change_directory('C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)').

yes
| ?- [arithmetic].
compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/arithmetic.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/arithmetic.pl compiled, 80 lines read - 1663 bytes written, 4 ms

yes
| ?- sum(69,0), sub(69,0), mul(69,1), div(69,1).
69
69
69
69.0

yes

*/

/*

In Prolog, the comma operator (,) means "and then":
It sequences two or more goals that must both succeed in order for the whole expression to succeed.



?- mul(99,2), sum(10,1).
Your definitions:

mul(X,Y):- M is X*Y, write(M).
sum(X,Y):- S is X+Y, write(S).
So mul(99,2) will compute M = 198 and print 198.

Then sum(10,1) will compute S = 11 and print 11.

Since both predicates use write/1, and write does not insert a space or newline, the console output looks like:


19811


*/