 
/*3.1 Write simple Facts for the statements and Querying it */
 
%query knowledge base 
/*CHECK THE STATEMENT 
PRIYA CAN COOK FOOD */
girl(priya). 
girl(tiyasha). 
girl(jaya). 
can_cook(priya). 


/* Output:- 
| ?- change_directory('C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)').

yes
| ?- [basics].
compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics.pl compiled, 31 lines read - 538 bytes written, 11 ms

yes
| ?- girl(priya).

yes
| ?- girl(aze).

no
| ?- can_cook(Aze).

Aze = priya

yes
| ?- can_cook(aze).

no
| ?- can_cook(priya).

yes

*/

/*

✅ Prolog Naming Rules – Key Concept
Atoms (constants): Start with a lowercase letter or are enclosed in single quotes.

Examples: priya, aze, 'Aze', 'Priya'

Variables: Start with an uppercase letter or underscore.

Examples: Aze, X, _Var

💡 So what happens here?
1. You define facts:
prolog
Copy
Edit
% basics.pl

girl(priya).
girl(tiyasha).
girl(jaya).
can_cook(priya).
2. Query: can_cook(Aze).
Aze starts with a capital, so Prolog treats it as a variable.

This means: “Is there any value for Aze such that can_cook(Aze) is true?”

Prolog looks for matches in the facts:

It finds can_cook(priya), so it binds Aze = priya.

3. Query: can_cook(aze).
aze is lowercase, so Prolog treats it as a constant (atom).

It searches for a fact like can_cook(aze). — no such fact exists.

So it returns no.

✅ Full Working Example (basics.pl):
prolog
Copy
Edit
% Facts
girl(priya).
girl(tiyasha).
girl(jaya).
can_cook(priya).
✅ Queries and Expected Output:
prolog
Copy
Edit
?- can_cook(Aze).
Aze = priya.          % Aze is a variable, Prolog finds priya as the only match.

?- can_cook(aze).
false.                % aze is a constant, not defined in any fact.

?- can_cook('Aze').
false.                % 'Aze' is also a constant (an atom), not defined.

?- can_cook(priya).
true.                 % priya is a constant that matches the fact.
🧪 Want to test this?
If you run this in a Prolog environment (like SWI-Prolog):

prolog
Copy
Edit
| ?- [basics].
| ?- can_cook(Aze).
Aze = priya.

| ?- can_cook(aze).
false.

| ?- can_cook('Aze').
false.
🎯 Summary
Prolog variables (uppercase): used to search for matches.

Prolog constants/atoms (lowercase or quoted): used to check for exact matches.

can_cook(Aze) finds anything/someone who can cook.

can_cook(aze) asks if a specific person/thing (aze) can cook.

*/