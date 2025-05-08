%check with query 
/*
 
RAM LIKES THE MANGO 
BILL LIKES CINDY 
JOHN OWNS GOLD 
A ROSE IS RED COLOUR 
 
*/
 
/*

% PROGRAM 
 
likes(ram ,mango). 
girl(seema). 
red(rose). 
likes(bill,cindy). 
owns(john ,gold).

compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics3.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics3.pl:16: warning: discontiguous predicate likes/2 - clause ignored
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics3.pl compiled, 23 lines read - 693 bytes written, 6 ms

*/

% PROGRAM 

likes(bill,cindy).
likes(ram ,mango). 
girl(seema). 
red(rose). 
 
owns(john ,gold).

/*
OUTPUT

GNU Prolog 1.5.0 (64 bits)
Compiled Jul  8 2021, 12:22:53 with gcc
Copyright (C) 1999-2021 Daniel Diaz

| ?- change_directory('C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)').

yes
| ?- [basics3].
compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics3.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics3.pl compiled, 118 lines read - 782 bytes written, 4 ms

yes
| ?- likes(bill,cindy).

yes
| ?- likes(ram ,mango), likes(bill,cindy).

yes
| ?- girl(seema), red(rose). 

yes
| ?-  girl(aze), red(rose). 

no

*/



/*

 
% PROGRAM 
 
likes(ram ,mango). 
girl(seema). 
red(rose). 
likes(bill,cindy). 
owns(john ,gold).

compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics3.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics3.pl:16: warning: discontiguous predicate likes/2 - clause ignored
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics3.pl compiled, 23 lines read - 693 bytes written, 6 ms

The warning you're seeing:

warning: discontiguous predicate likes/2 - clause ignored
means that you defined likes/2 in non-contiguous lines in your program — i.e., Prolog encountered multiple clauses of the same predicate, but they were separated by other predicate definitions.

🔍 What Does “Discontiguous Predicate” Mean?
In Prolog, all clauses for the same predicate (like likes/2) should be grouped together. If they are not, GNU Prolog will:

Give a warning

And possibly ignore the later clauses

✅ Example of Correct Usage (Grouped Together):


% Correct: all `likes/2` clauses are together
likes(ram, mango).
likes(bill, cindy).

girl(seema).
red(rose).
owns(john, gold).
❌ Example That Causes the Warning:

likes(ram, mango).

girl(seema).
red(rose).

likes(bill, cindy).  % <-- This will cause a "discontiguous predicate" warning

owns(john, gold).
🛠 How to Fix It
Move all likes/2 facts together, like this:


% PROGRAM

likes(ram, mango).
likes(bill, cindy).

girl(seema).
red(rose).
owns(john, gold).
Alternatively, you can suppress the warning (not recommended unless necessary) by adding this directive above your likes/2 definitions:


:- discontiguous likes/2.
But the best practice is to keep related facts and rules together to avoid confusion and errors.

OUTPUT:
(16 ms) yes
| ?- likes(bill,cindy).

no
| ?- likes(ram ,mango).

yes

*/