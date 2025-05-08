%Rules

/*
 
We can define rule as an implicit relationship between objects. So facts are conditionally true. So when one 
associated condition is true, then the predicate is also true.  
Suppose we have some rules as given below − 
 Lili is happy if she dances. 
 Tom is hungry if he is searching for food. 
 Jack and Bili are friends if both of them love to play cricket. 
 will go to play if school is closed, and he is free. 

*/


 
%Program 


% Facts
dances(lili).
search_for_food(tom).
lovesCricket(jack).
lovesCricket(bili).
isClosed(school).
free(ryan).

% Rules
happy(lili) :- dances(lili).
hungry(tom) :- search_for_food(tom).
friends(jack, bili) :- lovesCricket(jack), lovesCricket(bili).
goToPlay(ryan) :- isClosed(school), free(ryan).

 


/*
OUTPUT

GNU Prolog 1.5.0 (64 bits)
Compiled Jul  8 2021, 12:22:53 with gcc
Copyright (C) 1999-2021 Daniel Diaz

| ?- change_directory('C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)').

yes
| ?- [rules].
compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/rules.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/rules.pl compiled, 39 lines read - 1815 bytes written, 6 ms

yes
| ?- happy(lili).

yes
| ?- friends(X, Y).

X = jack
Y = bili

yes
| ?- hungry(tom).

yes
| ?- friends(jack, bili).

yes
| ?- goToPlay(ryan).

yes
| ?- goToPlay(tom).

no

*/



/*

🧠 Why Facts Are Needed Along with Rules
Rules in Prolog describe how something can be true, but they don’t guarantee it is true. For Prolog to conclude something from a rule, it needs facts to support the rule's conditions.

⚖️ Analogy: Think of a Rule as a Recipe
Example:
prolog
Copy
Edit
happy(lili) :- dances(lili).
This says:

“Lili is happy if she dances.”

But if you don’t know (i.e., don’t state) that dances(lili). is true, Prolog can’t conclude that happy(lili) is true — it doesn’t assume anything.

⚠️ Prolog Doesn’t “Guess” Facts
Unlike procedural languages, Prolog:

Doesn't assume missing facts are true or false.

Only knows what you explicitly tell it (facts), and how to relate things (rules).

Uses backward chaining to try to prove your query, using available facts and rules.

✅ So: Rules = Logic, Facts = Evidence
Rule only: happy(lili) :- dances(lili).
→ Prolog knows how to decide if Lili is happy, but doesn’t know whether she dances.

Fact only: dances(lili).
→ Prolog knows Lili dances, but doesn’t know why that matters unless a rule connects it.

Both: Now Prolog can say with confidence that happy(lili) is true.

*/