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
/* Or we can directly type "animal(X) :- dog(X); cat(X)."*/

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

/*

animal(X) :- dog(X).
animal(Y) :- cat(Y).
And you're asking:

Since we specified X and Y differently, why do we still get all results from both dog/1 and cat/1 when we query animal(X) or animal(Y)?

💡 The Key Idea: Variable Names Are Local to Each Rule or Query
In Prolog, variable names don’t carry meaning across rules unless explicitly linked.

So your two rules:

prolog
Copy
Edit
animal(X) :- dog(X).
animal(Y) :- cat(Y).
Are interpreted independently by Prolog as:

"animal(_) is true if dog(_) is true"

"animal(_) is true if cat(_) is true"

✅ When You Query:
Case 1: ?- animal(X).
This query says:

“Give me all X such that animal(X) is true.”

Prolog looks at both rules:

First rule: animal(X) :- dog(X).
→ tries dog(X) and finds sam, henry

Second rule: animal(Y) :- cat(Y).
→ finds felix, jame, michael, and binds them to X in your query result

💡 Even though you used Y in the rule, Prolog maps the result back to your query variable (X).

So you'll get:

ini
Copy
Edit
X = sam ;
X = henry ;
X = felix ;
X = jame ;
X = michael
Case 2: ?- animal(Y).
Same idea — just your query is now using Y, so Prolog unifies its answers with Y.

🧠 Rule of Thumb
Variable names inside rules are local to that rule

Variable names in queries are what Prolog uses to return answers

What matters is how Prolog unifies those variables during execution

🛠 Better Style Tip
To avoid confusion and make the logic clearer, it’s best to use the same variable name when defining multiple clauses of the same predicate. So instead of:

prolog
Copy
Edit
animal(X) :- dog(X).
animal(Y) :- cat(Y).
Prefer:

prolog
Copy
Edit
animal(X) :- dog(X).
animal(X) :- cat(X).
Now it's clearer that both rules produce values for animal(X).

*/
