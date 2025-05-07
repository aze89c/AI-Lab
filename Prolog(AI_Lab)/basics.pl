 
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

/*
To compile the GNU Prolog logic written code, primarily, it's considered a best practice to write this into the notepad and saving it with ".pl" extension. 

While compiling, in GNU Prolog, again, primarily you'll need the GNU Prolog console installed, it's lightweight and without any admin related options to select, which is comparatively easier to setup. 

So, to start the compilation, open the GNU Prolog console , select "File > Change Dir  > Select the folder (specific path of the file saved)". If it displays"yes", voila, you have selected the correct one(it'll display mostly a "yes" compiler reply for almost any directory change, but the problem will mostly occur in actually compiling the file which won't be available if you've saved it in any other directory)".

Next, you enter your filename, if the directory is read, in "[]." braces, note that the "dot" operator is mandatory for the execution of any statement/rules/syntactical entry. Say, your filename was "prolog1.pl"("pl" extension for  Prolog, written in notepad and saved with the said extension), so the step would look similar or very much like:
| ?- [prolog1].

If yes, continue with the logic based statements and rules for further development and execution. Else, check again for the directory read or the incorrect filename.

Now, for the for the final step, continue and have fun with your rules and conditions to be checked, verified and executed. If, in accordance with the logic, it'll return "yes", else a plain "no".

Example, in the above example it is particularly stated that "priya is a girl and can cook". Thus, appropriate syntactical logic was written and other names were included for the list of girls. Any out of logic or rule will be displayed false as it's not added as an input.

However, that's just the simple use cases and basic predefined logics, you can even perform arithmetic operations and apply complex "family tree" logic based rules and condition for further provisions. 

Again, while the concepts itself are fun and intriguing, Prolog is a really old language and has lost its variety of applications, but it was and will remain an OG for the development of AI in propositional logics and logic building.

*/

