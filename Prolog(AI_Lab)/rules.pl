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
 
happy(lili) :- dances(lili). 
hungry(tom) :- search_for_food(tom). 
friends(jack, bili) :- lovesCricket(jack), lovesCricket(bili). 
goToPlay(ryan) :- isClosed(school), free(ryan). 

/*
OUTPUT

*/